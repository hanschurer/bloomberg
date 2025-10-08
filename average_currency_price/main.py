'''
data_list = {
    ("BankA", "USD", 7.2),
    ("BankB", "USD", 7.3),
    ("BankC", "EUR", 8.0),
    ("BankA", "USD", 7.5),  # 覆盖前一个 BankA 的 USD 价格
}
'''
from collections import defaultdict
from typing import Dict


class CurrencyPrice:
    def __init__(self):
        self.currency_data = defaultdict(lambda: defaultdict(float))
        self.currency_sum = defaultdict(float)

    def add_data(self, data) -> None:
        bank, currency, price = data
        prev_price = self.currency_data[currency][bank]
        self.currency_data[currency][bank] = price
        self.currency_sum[currency] += price - prev_price

    def average_price(self) -> Dict[str, float]:
        avg_price = {}
        for currency, total in self.currency_sum.items():
            avg_price[currency] = total / len(self.currency_data[currency])
        return avg_price

if __name__ == "__main__":
    data_list = [
        ("BankA", "USD", 7.2),
        ("BankB", "USD", 7.3),
        ("BankC", "EUR", 8.0),
        ("BankA", "USD", 7.5),  # 覆盖前一个 BankA 的 USD 价格
    ]

    cp = CurrencyPrice()
    for data in data_list:
        cp.add_data(data)

    print(cp.average_price())
    # 输出: {'USD': 7.4, 'EUR': 8.0}
