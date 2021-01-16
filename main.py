from dealer import *
from account import Account
from workspace import ExcelWorkSpace
import logging

dealer_map = {
    "华泰": Huatai(),
    "招证": Marchants(),
    "长桥": LongBridge(),
    "广发": GFHK(),
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
