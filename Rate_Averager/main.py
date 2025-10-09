'''
source: GPT 根据群友聊天记录总结的题目

1. Problem Description
You are tasked with designing a class to track real-time foreign exchange (FX) rates from multiple banks. The system will
receive a continuous stream of rate updates and must be able to provide the average rate for each currency across all
reporting banks at any given moment. The data comes in the format of (Bank Name, Currency Code, Rate).
The system needs to handle new data, updates to existing data, and calculate averages efficiently.

2. Requirements
Implement a class named FxRateTracker with the following methods:
    2.1. add_rate(self, bank: str, currency: str, rate: float) -> None:
    This method adds or updates a currency rate. It should handle three scenarios seamlessly:
    -   A new currency is introduced.
    -   A new bank starts providing a rate for an existing currency.
    -   An existing bank updates its rate for a currency.

    2.2. display_average_rates(self) -> None:
    This method calculates and prints the average rate for each currency currently being tracked.
    The output should be clear and easy to read, for example: CURRENCY: AVERAGE_RATE.

3. Rules and Clarifications
Update Rule: If a rate is provided for a (bank, currency) pair that already exists, the new rate overrides the previous
one. It is considered an update, not a new entry.

Average Calculation Rule: The average rate for a given currency is defined as the sum of the latest rates from all
unique banks providing that currency, divided by the number of those unique banks.

4. Performance Considerations
The add_rate operation should be as efficient as possible.
The calculation of averages within the display_average_rates method should ideally be O(1) for each currency, meaning
the running totals and counts should be maintained during the add_rate operation.


5. Example
tracker = FxRateTracker()
tracker.add_rate("BankA", "USD", 7.2)
tracker.add_rate("BankB", "USD", 7.3)
tracker.add_rate("BankC", "EUR", 8.0)
tracker.add_rate("BankA", "USD", 7.5) # This is an update

A call to tracker.display_average_rates() should produce the following output:
USD: 7.4
EUR: 8.0
'''
import math
from collections import defaultdict


class BankCurrency:
    def __init__(self, bank: str = "BankA"):
        self.bank = bank
        self.currency_dict = defaultdict(float)

    def update(self, currency: str, rate: float):
        self.currency_dict[currency] = rate

    # return True if this is new currency type
    # return False if it exits
    def check_new_currency(self, currency: str):
        return currency not in self.currency_dict


class FxRateTracker:
    def __init__(self):
        # class attributes
        # map bank to its currency and rate
        # key: bank id, value: BankCurrency Object
        self.bank_map = defaultdict(BankCurrency)
        # key: currency type, value: [total, count] -> calculate average
        self.currency_map = defaultdict(list)

    # TODO: update operation
    def add_rate(self, bank: str, currency: str, rate: float) -> None:
        # first add bank
        if bank not in self.bank_map:
            item = BankCurrency(bank)
            item.update(currency, rate)
            self.bank_map[bank] = item
        else:
            # whether to add new currency
            item = self.bank_map[bank]
            if item.check_new_currency(currency):
                item.update(currency, rate)
            # update existing currency
            else:
                # clear the odd currency in counting map
                prev_rate = item.currency_dict[currency]
                # update the count and total sum
                self.currency_map[currency][0] -= prev_rate
                self.currency_map[currency][1] -= 1
                item.update(currency, rate)

        # first add the currency
        if currency not in self.currency_map:
            self.currency_map[currency] = [rate, 1]
        else:
            total, count = self.currency_map[currency]
            self.currency_map[currency] = [total + rate, count + 1]

    def display_average_rates(self) -> dict:
        result = {}
        for currency, (total, count) in self.currency_map.items():
            if count > 0:
                result[currency] = round(total / count, 2)
        return result


# ---------------- 测试工具函数 ----------------
def run_test(description, actual, expected):
    result = "PASS" if actual == expected else "FAIL"
    print(f"{description}: Expected={expected}, Actual={actual} --> {result}")


# ---------------- 主函数测试 ----------------
if __name__ == "__main__":
    tracker = FxRateTracker()

    print("=== Case 1: 基础示例 ===")
    tracker.add_rate("BankA", "USD", 7.2)
    tracker.add_rate("BankB", "USD", 7.3)
    tracker.add_rate("BankC", "EUR", 8.0)
    tracker.add_rate("BankA", "USD", 7.5)  # 更新

    avg_rates = tracker.display_average_rates()
    run_test("USD 平均值", avg_rates["USD"], 7.40)
    run_test("EUR 平均值", avg_rates["EUR"], 8.00)

    print("\n=== Case 2: 新银行加入 ===")
    tracker.add_rate("BankD", "USD", 7.1)
    avg_rates = tracker.display_average_rates()
    run_test("USD 平均值 (3家银行)", avg_rates["USD"], round((7.5 + 7.3 + 7.1) / 3, 2))

    print("\n=== Case 3: 同一银行新增新货币 ===")
    tracker.add_rate("BankA", "JPY", 110.0)
    avg_rates = tracker.display_average_rates()
    run_test("JPY 平均值", avg_rates["JPY"], 110.0)

    print("\n=== Case 4: 更新已有货币 ===")
    tracker.add_rate("BankB", "USD", 7.6)  # 更新 BankB 的 USD
    avg_rates = tracker.display_average_rates()
    run_test("USD 平均值 (更新后)", avg_rates["USD"], round((7.5 + 7.6 + 7.1) / 3, 2))
