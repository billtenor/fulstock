from action import *
from functools import reduce
import logging


class Stock(object):
    class StockHold(object):
        def __init__(self, unit_price, quantity):
            self.unit_price_map = {
                unit_price: quantity
            }

        def buy(self, unit_price, quantity):
            if unit_price not in self.unit_price_map:
                self.unit_price_map[unit_price] = 0
            self.unit_price_map[unit_price] += quantity

        def sell(self, unit_price, quantity):
            profit = 0
            for buy_unit_price, buy_quantity in self.unit_price_map.items():
                if buy_quantity == 0:
                    continue
                if quantity == 0:
                    break
                sell_quantity = min(quantity, buy_quantity)
                profit += (unit_price - buy_unit_price) * sell_quantity
                self.unit_price_map[buy_unit_price] -= sell_quantity
                quantity -= sell_quantity
            return profit

        def quantity(self):
            return reduce(lambda x, y: x + y,
                          [quantity for quantity in self.unit_price_map.values()])

        def price(self):
            return reduce(lambda x, y: x + y,
                          [unit_price * quantity for unit_price, quantity in self.unit_price_map.items()])

    def __init__(self, name):
        # 股票名称
        self.name = name
        # 打新手数
        self.subscribe_count = 0
        # 打新账户数
        self.subscribe_dealer_map = {}
        # 中签手数
        self.allotment_count = 0
        # 中签期望
        self.allotment_expect = 0
        # 现金占用
        self.cash_use = 0
        # 认购成本
        self.allotment_cost = 0
        # 交易成本
        self.trade_cost = 0
        # 资金调拨成本
        self.transfer_cost = 0
        # 交易利润
        self.trade_profit = 0
        # 持仓
        self.hold = {}

    def add_action(self, dealer, action, cost):
        if isinstance(action, BuyingAction):
            self.trade_cost += cost
            if dealer not in self.hold:
                self.hold[dealer] = self.StockHold(action.unit_price, action.quantity)
            else:
                self.hold[dealer].buy(action.unit_price, action.quantity)
        elif isinstance(action, SellingAction):
            try:
                self.trade_profit += self.hold[dealer].sell(action.unit_price, action.quantity)
                self.trade_cost += cost
            except Exception as e:
                logging.error("超卖 %s, 价格: %d, 数量: %d", self.name, action.unit_price, action.quantity)

        elif isinstance(action, SubScribeAction):
            self.subscribe_dealer_map[dealer] = 1
            self.subscribe_count += action.quantity
            self.allotment_expect += (action.allotment_target - 1 + 1 * action.allotment_rate)
            self.cash_use += action.quantity * action.unit_price * (1 - action.margin_rate)
            self.allotment_cost += cost
        elif isinstance(action, AllotmentAction):
            self.allotment_count += action.quantity
            self.allotment_cost += cost
            if dealer not in self.hold:
                self.hold[dealer] = self.StockHold(action.unit_price, action.quantity)
            else:
                self.hold[dealer].buy(action.unit_price, action.quantity)

    def price(self):
        return reduce(lambda x, y: x + y, [0] + [hold.price() for hold in self.hold.values()])

    def quantity(self):
        return reduce(lambda x, y: x + y, [0] + [hold.quantity() for hold in self.hold.values()])

    def unit_cost(self):
        quantity = self.quantity()
        if quantity != 0:
            return self.price() / self.quantity()
        else:
            return 0

    def subscribe_account_count(self):
        return len(self.subscribe_dealer_map)
