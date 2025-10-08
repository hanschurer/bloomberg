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