class BuyingAction(object):
    """
    交易买入
    """

    def __init__(self, quantity, unit_price):
        self.quantity = quantity
        self.unit_price = unit_price


class SellingAction(object):
    """
    交易卖出
    """

    def __init__(self, quantity, unit_price):
        self.quantity = quantity
        self.unit_price = unit_price


class SubScribeAction(object):
    """
    申购
    """

    def __init__(self, quantity, unit_price, margin_rate,
                 interest=0.0, discounts=0.0,
                 allotment_target=1, allotment_rate=0.0):
        self.quantity = quantity
        self.unit_price = unit_price
        self.margin_rate = margin_rate
        self.interest = interest
        self.discounts = discounts
        self.allotment_rate = allotment_rate
        self.allotment_target = allotment_target


class AllotmentAction(object):
    """
    中签
    """

    def __init__(self, quantity, unit_price):
        self.quantity = quantity
        self.unit_price = unit_price


class WithdrawalAction(object):
    """
    提款
    """

    def __init__(self, amount, addition=0.0):
        self.amount = amount
        self.addition = addition


class DepositAction(object):
    """
    存款
    """

    def __init__(self, amount, addition=0.0):
        self.amount = amount
        self.addition = addition


class PaymentAction(object):
    """
    付款
    """

    def __init__(self, name, payment):
        self.name = name
        self.payment = payment
