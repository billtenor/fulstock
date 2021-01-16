from openpyxl import load_workbook
from action import *
from stock import Stock
from functools import reduce
import logging


class ActionRow(object):
    def __init__(self, row):
        self.time = row[0].value
        self.dealer = row[1].value
        self.action = row[2].value
        self.stock_name = row[3].value
        self.quantity = row[4].value
        self.unit_price = row[5].value
        self.fee = row[6]
        self.margin_rate = row[7].value
        self.interest = 0.0 if row[8].value is None else row[8].value
        self.discounts = 0.0 if row[9].value is None else row[9].value
        self.allotment_target = 1 if row[10].value is None else row[10].value
        self.allotment_rate = 0 if row[11].value is None else row[11].value
        self.amount = row[12].value
        self.addition = 0.0 if row[13].value is None else row[13].value
        self.name = row[14].value
        self.payment = row[15].value

    def parse_action(self):
        if self.action == '买入':
            return BuyingAction(self.quantity, self.unit_price)
        elif self.action == '卖出':
            return SellingAction(self.quantity, self.unit_price)
        elif self.action == '认购':
            return SubScribeAction(self.quantity, self.unit_price,
                                   self.margin_rate, self.interest, self.discounts,
                                   self.allotment_target, self.allotment_rate)
        elif self.action == '中签':
            return AllotmentAction(self.quantity, self.unit_price)
        elif self.action == '入金':
            return WithdrawalAction(self.amount, self.addition)
        elif self.action == '出金':
            return DepositAction(self.amount, self.addition)
        elif self.action == '支出':
            return DepositAction(self.name, self.payment)
        else:
            return None

    def set_fee(self, fee):
        self.fee.value = fee

    def get_dealer_name(self):
        return self.dealer

    def get_stock_name(self):
        return self.stock_name


class StockRow(object):
    def __init__(self, row):
        self.stock_code = row[0].value
        self.stock_name = row[1].value
        self.hand_count = 0 if row[4].value is None else row[4].value
        self.unit_price = row[4].value * row[5].value \
            if row[4].value is not None and row[5].value is not None else 0
        self.unit_cost = row[6]
        self.subscribe_count = row[7]
        self.subscribe_account_count = row[8]
        self.allotment_count = row[9]
        self.allotment_expect = row[11]
        self.hold_count = row[12]
        self.cash_use = row[13]
        self.allotment_cost = row[14]
        self.trade_cost = row[15]
        self.transfer_cost = row[16]
        self.floating_profit = row[17]
        self.trade_profit = row[18]

    def update(self, stock):
        self.unit_cost.value = stock.unit_cost() / self.hand_count if self.hand_count != 0 else 0
        self.subscribe_count.value = stock.subscribe_count
        self.subscribe_account_count.value = stock.subscribe_account_count()
        self.allotment_count.value = stock.allotment_count
        self.allotment_expect.value = stock.allotment_expect
        hold_count = stock.quantity()
        self.hold_count.value = hold_count
        self.cash_use.value = stock.cash_use
        self.allotment_cost.value = stock.allotment_cost
        self.trade_cost.value = stock.trade_cost
        self.floating_profit.value = hold_count * self.unit_price - stock.price()
        self.trade_profit.value = stock.trade_profit
        self.transfer_cost.value = stock.transfer_cost


class ExcelWorkSpace(object):
    def __init__(self, dealer_map, account_map, file_path):
        self.dealer_map = dealer_map
        self.account_map = account_map
        self.file_path = file_path
        self.workbook = load_workbook(self.file_path)
        sheet_names = self.workbook.get_sheet_names()
        self.action_sheets = {}
        self.stock_map = {}
        for name in sheet_names:
            if name.find("操作") != -1:
                self.action_sheets[name] = self.workbook[name]
        self.stock_sheet = self.workbook["股票分析"]

    def update(self):
        for sheet_name, action_sheet in self.action_sheets.items():
            self._action_update(sheet_name, action_sheet)
        self._stock_update(self.stock_sheet)
        self.workbook.save(self.file_path)

    def _stock_update(self, stock_sheet):
        update_count = 0
        for row in self._iter_sheet_rows(stock_sheet, 1):
            stock_row = StockRow(row)
            if stock_row.stock_name in self.stock_map:
                stock_row.update(self.stock_map[stock_row.stock_name])
                update_count += 1
        logging.info("stock update count: %d", update_count)

    def _action_update(self, sheet_name, action_sheet):
        update_count = 0
        for row in self._iter_sheet_rows(action_sheet, 1):
            action_row = ActionRow(row)
            dealer_name = action_row.get_dealer_name()
            stock_name = action_row.get_stock_name()
            if stock_name not in self.stock_map:
                self.stock_map[stock_name] = Stock(stock_name)
            if dealer_name not in self.dealer_map:
                continue
            dealer = self.dealer_map[dealer_name]
            action = action_row.parse_action()
            if action is None:
                continue
            fee = dealer.fee(action)
            action_row.set_fee(fee)
            self.stock_map[stock_name].add_action(dealer_name, action, fee)
            update_count += 1
        logging.info("sheet %s action update count: %d", sheet_name, update_count)

    def _iter_sheet_rows(self, sheet, start_row):
        row_index = 0
        for row in sheet.rows:
            if row_index < start_row:
                row_index += 1
                continue
            else:
                row_index += 1
                yield row
