from dealer import *
from account import Account
from workspace import ExcelWorkSpace
import logging

dealer_map = {
    "华泰": Huatai(),
    "招证": Marchants(),
    "长桥": LongBridge(),
    "广发": GFHK(),
    "辉立": Phillip(),
    "华盛": Valuable(),
    "致富": Chief(),
    "尊嘉": Junior(),
    "佳兆业": Kaisa(),
    "富途": Futu(),
    "东财": EastMoney(),
    "方德": Forthright(),
    "盈立": USmart(),
    "青石": BlueStone(),
    "艾德": Eddid(),
    "富昌": Fulbright(),
    "东方": Orient(),
    "阿尔法": Alpha(),
    "富利": Richbays(),
    "富元": Jiufu(),
    "国信": Guosen(),
    "微牛": Webull(),
    "利弗莫尔": Livermore(),
    "有鱼": Yunfeng(),
    "直达": DirectAccess(),
    "耀才": BrightSmart(),
}

account_map = {account.name: account for account in [
    Account("bill-华泰"),
    Account("bill-招证"),
]}

logging.basicConfig(level=logging.INFO, format='%(levelname)s %(asctime)s %(filename)s:%(lineno)d] %(message)s')


def main():
    work_space = ExcelWorkSpace(dealer_map=dealer_map, account_map=account_map, file_path="fulstock.xlsx")
    work_space.update()


if __name__ == '__main__':
    main()
