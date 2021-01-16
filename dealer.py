from dealer_base import DealerBase


class Marchants(DealerBase):
    def __init__(self):
        super(Marchants, self).__init__("招证香港财经")
        self.commission_rate = 0.25 / 100
        self.commission_min = 100
        self.cash_ipo_handing_fee = 100
        self.loan_ipo_handing_fee = 100


class Huatai(DealerBase):
    def __init__(self):
        super(Huatai, self).__init__("华泰金融")
        self.commission_rate = 0
        self.commission_min = 0
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 0


class LongBridge(DealerBase):
    def __init__(self):
        super(LongBridge, self).__init__("长桥")
        self.commission_rate = 0.028 / 100
        self.commission_min = 15
        self.cash_ipo_handing_fee = 49
        self.loan_ipo_handing_fee = 99


class GFHK(DealerBase):
    def __init__(self):
        super(GFHK, self).__init__("广发证券")
        self.commission_rate = 0.25 / 100
        self.commission_min = 100
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 100
