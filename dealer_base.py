import math
from action import *


class DealerBase(object):
    def __init__(self, name):
        self.name = name
        # 交易经纪佣金
        self.commission_rate = 0.25 / 100
        self.commission_min = 100.0
        # 平台使用费
        self.platform_fee = 0.0
        # 印花税率, 印花税不足一元作一元计
        self.stamp_rate = 0.1 / 100
        # 交易证收费
        self.SFC_levy_rate = 0.0027 / 100
        # 联交所交易费
        self.trading_fee_rate = 0.005 / 100
        # 中央结算系统交收费
        self.clearing_fee_rate = 0.005 / 100
        self.clearing_fee_min = 2
        self.clearing_fee_max = 100
        # 中签费率
        self.ipo_allotment_rate = 1.0077 / 100
        # 现金申购手续费
        self.cash_ipo_handing_fee = 0
        # 融资申购手续费
        self.loan_ipo_handing_fee = 100
        # 入金手续费
        self.withdrawal_fee = 0
        # 出金手续费
        self.deposit_fee = 0

    def fee(self, action):
        if isinstance(action, BuyingAction) or isinstance(action, SellingAction):
            return self._trade_fee(action)
        elif isinstance(action, SubScribeAction):
            return self._subscribe_fee(action)
        elif isinstance(action, AllotmentAction):
            return self._allotment_fee(action)
        elif isinstance(action, WithdrawalAction):
            return self._withdrawal_fee(action)
        elif isinstance(action, DepositAction):
            return self._deposit_fee(action)
        else:
            return 0.0

    def _subscribe_fee(self, action):
        handing_fee = self.cash_ipo_handing_fee if action.margin_rate == 0 else self.loan_ipo_handing_fee
        fee = handing_fee + action.interest - action.discounts
        return round(fee, 2)

    def _allotment_fee(self, action):
        amount = action.quantity * action.unit_price
        return round(amount * self.ipo_allotment_rate, 2)

    def _withdrawal_fee(self, action):
        return self.withdrawal_fee + action.addition

    def _deposit_fee(self, action):
        return self.deposit_fee + action.addition

    def _trade_fee(self, action):
        amount = action.quantity * action.unit_price
        platform_fee = self.platform_fee
        commission = round(max(amount * self.commission_rate, self.commission_min), 2)
        stamp = math.ceil(amount * self.stamp_rate)
        SFC_levy = round(amount * self.SFC_levy_rate, 2)
        trading_fee = round(amount * self.trading_fee_rate, 2)
        clearing_fee = round(min(self.clearing_fee_max, max(self.clearing_fee_min, amount * self.clearing_fee_rate)), 2)
        return platform_fee + commission + stamp + SFC_levy + trading_fee + clearing_fee
