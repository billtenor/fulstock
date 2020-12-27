from openpyxl import load_workbook
from action import *
import logging


class ActionRow(object):
    def __init__(self, row):
        self.time = row[0].value
        self.dealer = row[1].value
        self.action = row[2].value
        self.stock = row[3].value
        self.quantity = row[4].value
        self.unit_price = row[5].value
        self.fee = row[6]
        self.margin_rate = row[7].value
        self.interest = 0.0 if row[8].value is None else row[8].value
        self.discounts = 0.0 if row[9].value is None else row[9].value
        self.amount = row[10].value
        self.addition = 0.0 if row[11].value is None else row[11].value
        self.name = row[12].value
        self.payment = row[13].value

    def parse_action(self):
        if self.action == '买入':
            return BuyingAction(self.quantity, self.unit_price)
        elif self.action == '卖出':
            return SellingAction(self.quantity, self.unit_price)
        elif self.action == '认购':
            return SubScribeAction(self.quantity, self.unit_price, self.margin_rate, self.interest, self.discounts)
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


class ExcelWorkSpace(object):
    def __init__(self, dealer_map, account_map, file_path):
        self.dealer_map = dealer_map
        self.account_map = account_map
        self.file_path = file_path
        self.workbook = load_workbook(self.file_path)
        self.action_sheet = self.workbook["操作记录"]

    def update(self):
        self._action_update()
        self.workbook.save(self.file_path)

    def _action_update(self):
        update_count = 0
        for row in self._iter_sheet_rows(self.action_sheet, 1):
            action_row = ActionRow(row)
            dealer_name = action_row.get_dealer_name()
            if dealer_name not in self.dealer_map:
                continue
            dealer = self.dealer_map[dealer_name]
            action = action_row.parse_action()
            if action is None:
                continue
            fee = dealer.fee(action)
            action_row.set_fee(fee)
            update_count += 1
        logging.info("action update count: %d", update_count)

    def _iter_sheet_rows(self, sheet, start_row):
        row_index = 0
        for row in sheet.rows:
            if row_index < start_row:
                row_index += 1
                continue
            else:
                row_index += 1
                yield row
