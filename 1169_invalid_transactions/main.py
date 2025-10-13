# — Title: Flag Invalid Card Transactions
# Difficulty: Medium
# Prompt: Given a list of credit card transactions with {name, time (minutes), amount, city}, return all transaction strings that are invalid. A transaction is invalid if amount > 1000 or if the same name has transactions in different cities within ±60 minutes.
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans = [x.split(',') for x in transactions]
        res = []
        for i in range(len(trans)):
            name, time, money, city = trans[i]
            time = int(time)
            if int(money) > 1000:
                res.append(transactions[i])
                continue
            for j in range(len(trans)):
                if i == j:
                    continue
                name1, time1, money1, city1 = trans[j]
                if name1 == name and city1 != city and abs(int(time1) - time) <= 60:
                    res.append(transactions[i])
                    break
        return res

