class Account(object):
    def __init__(self, name, fund=0.00, stock_count={}):
        self.name = name
        self.fund = fund
        self.stock_count = stock_count
