from dealer_base import DealerBase


class Marchants(DealerBase):
    def __init__(self):
        super(Marchants, self).__init__("招证香港财经")
        self.platform_fee = 0
        self.commission_rate = 0.25 / 100
        self.commission_min = 100
        self.cash_ipo_handing_fee = 100
        self.loan_ipo_handing_fee = 100


class Huatai(DealerBase):
    def __init__(self):
        super(Huatai, self).__init__("华泰金融")
        self.platform_fee = 0
        self.commission_rate = 0
        self.commission_min = 0
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 0
        self.deposit_fee = 35


class LongBridge(DealerBase):
    def __init__(self):
        super(LongBridge, self).__init__("长桥")
        self.platform_fee = 0
        self.commission_rate = 0.028 / 100
        self.commission_min = 15
        self.cash_ipo_handing_fee = 49
        self.loan_ipo_handing_fee = 99


class GFHK(DealerBase):
    def __init__(self):
        super(GFHK, self).__init__("广发证券")
        self.platform_fee = 0
        # TODO: 搞清楚交易费率, 不要猜
        self.commission_rate = 0.25 / 100
        self.commission_min = 100
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 100


# TODO: 修改详细规则
class Phillip(DealerBase):
    def __init__(self):
        super(Phillip, self).__init__("辉立证券")
        self.platform_fee = 0
        self.commission_rate = 0.25 / 100
        self.commission_min = 100
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 0


class Valuable(DealerBase):
    def __init__(self):
        super(Valuable, self).__init__("华盛证券")
        self.platform_fee = 15
        self.commission_rate = 0.03 / 100
        self.commission_min = 3
        self.cash_ipo_handing_fee = 50
        self.loan_ipo_handing_fee = 100


class Chief(DealerBase):
    def __init__(self):
        super(Chief, self).__init__("致富证券")
        self.platform_fee = 0
        self.commission_rate = 0.0675 / 100
        self.commission_min = 40
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 100


class Junior(DealerBase):
    def __init__(self):
        super(Junior, self).__init__("尊嘉证券")
        self.platform_fee = 1
        self.commission_rate = 0
        self.commission_min = 0
        self.cash_ipo_handing_fee = 5
        self.loan_ipo_handing_fee = 31.9
        self.deposit_fee = 10


class Kaisa(DealerBase):
    def __init__(self):
        super(Kaisa, self).__init__("佳兆业证券")
        self.platform_fee = 0
        self.commission_rate = 0.05 / 100
        self.commission_min = 15
        self.cash_ipo_handing_fee = 50
        self.loan_ipo_handing_fee = 80


class Futu(DealerBase):
    def __init__(self):
        super(Futu, self).__init__("富途证券")
        self.platform_fee = 15
        self.commission_rate = 0
        self.commission_min = 0
        self.cash_ipo_handing_fee = 50
        self.loan_ipo_handing_fee = 100


class EastMoney(DealerBase):
    def __init__(self):
        super(EastMoney, self).__init__("东财国际证券")
        self.platform_fee = 15
        self.commission_rate = 0.025 / 100
        self.commission_min = 5
        self.cash_ipo_handing_fee = 25
        self.loan_ipo_handing_fee = 100


class Forthright(DealerBase):
    def __init__(self):
        super(Forthright, self).__init__("方德证券")
        self.platform_fee = 0
        self.commission_rate = 0.25 / 100
        self.commission_min = 100
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 100


class USmart(DealerBase):
    def __init__(self):
        super(USmart, self).__init__("盈立证券")
        self.platform_fee = 12
        self.commission_rate = 0.03 / 100
        self.commission_min = 0
        self.cash_ipo_handing_fee = 18
        self.loan_ipo_handing_fee = 99


class BlueStone(DealerBase):
    def __init__(self):
        super(BlueStone, self).__init__("青石证券")
        self.platform_fee = 0
        self.commission_rate = 0.2 / 100
        self.commission_min = 40
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 50


class Eddid(DealerBase):
    def __init__(self):
        super(Eddid, self).__init__("艾德证券")
        self.platform_fee = 12
        self.commission_rate = 0.028 / 100
        self.commission_min = 8
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 100


class Fulbright(DealerBase):
    def __init__(self):
        super(Fulbright, self).__init__("富昌证券")
        self.platform_fee = 0
        self.commission_rate = 0.15 / 100
        self.commission_min = 75
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 38


class Orient(DealerBase):
    def __init__(self):
        super(Orient, self).__init__("东方证券")
        self.platform_fee = 0
        self.commission_rate = 0.25 / 100
        self.commission_min = 100
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 100


class Alpha(DealerBase):
    def __init__(self):
        super(Alpha, self).__init__("阿尔法证券")
        self.platform_fee = 15
        self.commission_rate = 0.03 / 100
        self.commission_min = 3
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 100


class Richbays(DealerBase):
    def __init__(self):
        super(Richbays, self).__init__("富利证券")
        self.platform_fee = 0
        self.commission_rate = 0.25 / 100
        self.commission_min = 50
        self.cash_ipo_handing_fee = 20
        self.loan_ipo_handing_fee = 60


class Jiufu(DealerBase):
    def __init__(self):
        super(Jiufu, self).__init__("富元证券")
        self.platform_fee = 0
        self.commission_rate = 0.029 / 100
        self.commission_min = 30
        self.cash_ipo_handing_fee = 10
        self.loan_ipo_handing_fee = 59


class Guosen(DealerBase):
    def __init__(self):
        super(Guosen, self).__init__("国信证券")
        self.platform_fee = 0
        self.commission_rate = 0.25 / 100
        self.commission_min = 100
        self.cash_ipo_handing_fee = 100
        self.loan_ipo_handing_fee = 100


class Webull(DealerBase):
    def __init__(self):
        super(Webull, self).__init__("微牛证券")
        self.platform_fee = 10
        self.commission_rate = 0
        self.commission_min = 0
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 0


class Livermore(DealerBase):
    def __init__(self):
        super(Livermore, self).__init__("利弗莫尔证券")
        self.platform_fee = 0
        self.commission_rate = 0.025 / 100
        self.commission_min = 3
        self.cash_ipo_handing_fee = 50
        self.loan_ipo_handing_fee = 100


class Yunfeng(DealerBase):
    def __init__(self):
        super(Yunfeng, self).__init__("有鱼证券")
        self.platform_fee = 0
        self.commission_rate = 0.1 / 100
        self.commission_min = 50
        self.cash_ipo_handing_fee = 100
        self.loan_ipo_handing_fee = 100


class DirectAccess(DealerBase):
    def __init__(self):
        super(DirectAccess, self).__init__("有鱼证券")
        self.platform_fee = 0
        self.commission_rate = 0.01 / 100
        self.commission_min = 5
        self.cash_ipo_handing_fee = 50
        self.loan_ipo_handing_fee = 100
        self.deposit_fee = 25


class BrightSmart(DealerBase):
    def __init__(self):
        super(BrightSmart, self).__init__("耀才证券")
        self.platform_fee = 0
        self.commission_rate = 0.01 / 100
        self.commission_min = 5
        self.cash_ipo_handing_fee = 0
        self.loan_ipo_handing_fee = 100
