class BuyingAction(object):
    def __init__(self, quantity, unit_price):
        self.quantity = quantity
        self.unit_price = unit_price


class SellingAction(object):
    def __init__(self, quantity, unit_price):
        self.quantity = quantity
        self.unit_price = unit_price


class SubScribeAction(object):
    def __init__(self, quantity, unit_price, margin_rate, interest=0.0, discounts=0.0):
        self.quantity = quantity
        self.unit_price = unit_price
        self.margin_rate = margin_rate
        self.interest = interest
        self.discounts = discounts


class AllotmentAction(object):
    def __init__(self, quantity, unit_price):
        self.quantity = quantity
        self.unit_price = unit_price


class WithdrawalAction(object):
    def __init__(self, amount, addition=0.0):
        self.amount = amount
        self.addition = addition


class DepositAction(object):
    def __init__(self, amount, addition=0.0):
        self.amount = amount
        self.addition = addition


class PaymentAction(object):
    def __init__(self, name, payment):
        self.name = name
        self.payment = payment
