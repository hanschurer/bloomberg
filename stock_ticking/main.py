'''

You are asked to design a data structure that supports two operations on stock trading volumes:

    1. addStocksVolume(string stockSymbol, int volume)
        Records a new trade volume for the given stock symbol.
        The volume for each stock is cumulative: if the same stock symbol is added multiple times, its total volume should be the sum of all added volumes.

    2.  topKstocks(int k)
        Returns the list of the k stock symbols with the highest cumulative trading volume.
        If two stocks have the same volume, you may return them in any order.

If there are fewer than k stocks in total, return all of them.

Your implementation should be efficient in both updating volumes and retrieving the top-k stocks.

Input Format:
    addStocksVolume("AAPL", 100)
    addStocksVolume("GOOG", 200)
    addStocksVolume("AAPL", 50)
    topKstocks(1)
    topKstocks(2)
Output Format:
    ["GOOG"]
    ["GOOG", "AAPL"]

'''
import heapq
from collections import defaultdict
#可以和面试官讨论，
# 1. 添加频率高， 用heap， 添加O1， 查询nlogK
# 2. 查询频率高， 用sortedList 切片只需要k的时间复杂度

class StockTrader:
    """
    一个数据结构，用于跟踪股票交易量并检索交易量最高的K只股票。
    """

    def __init__(self):
        """
        初始化一个哈希表来存储股票的累计交易量。
        使用 defaultdict 可以简化新股票的添加过程。
        """
        # self.volumes 映射: 股票代码 -> 累计交易量
        self.volumes = defaultdict(int)

    def addStocksVolume(self, stockSymbol: str, volume: int) -> None:
        """
        记录一只股票的新交易量，并累加到其总交易量中。
        这个操作的平均时间复杂度是 O(1)。
        """
        self.volumes[stockSymbol] += volume
        print(f"Added {volume} to {stockSymbol}. New total: {self.volumes[stockSymbol]}")

    def topKstocks(self, k: int) -> list[str]:
        """
        返回累计交易量最高的K只股票的代码列表。
        这个操作的时间复杂度是 O(N log K)，其中N是独特的股票总数。
        """
        # 创建一个最小堆来存储 (交易量, 股票代码) 对。
        # Python的 heapq 模块实现的是最小堆。
        min_heap = []

        # 遍历存储在哈希表中的所有股票。
        for stock, volume in self.volumes.items():
            # 将 (交易量, 股票代码) 元组推入堆中。
            heapq.heappush(min_heap, (volume, stock))

            # 如果堆的大小超过了K，就弹出具有最小交易量的元素。
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # 此时，堆中剩下的就是交易量最高的K个元素。
        # 我们从堆中提取股票代码。
        top_k_list = [stock for volume, stock in min_heap]

        # 题目对输出顺序没有要求，但通常我们会按从高到低的顺序列出。
        # 我们可以通过对堆中元素进行排序来实现。
        # sorted() 会先比较元组的第一个元素（volume），再比较第二个元素（stock）。
        # reverse=True 确保了按交易量从高到低排序。
        top_k_sorted = sorted(min_heap, key=lambda x: x[0], reverse=True)

        return [stock for volume, stock in top_k_sorted]



# --- 示例使用 ---
if __name__ == "__main__":
    tracker = StockTrader()
    tracker.addStocksVolume("AAPL", 100)
    tracker.addStocksVolume("GOOG", 200)
    tracker.addStocksVolume("AAPL", 50)

    print("\n--- Top K Stocks ---")

    # 检索交易量最高的1只股票
    top_1 = tracker.topKstocks(1)
    print(f"Top 1 stock: {top_1}")  # 预期输出: ["GOOG"]

    # 检索交易量最高的2只股票
    top_2 = tracker.topKstocks(2)
    print(f"Top 2 stocks: {top_2}")  # 预期输出: ["GOOG", "AAPL"]

    # 添加更多数据
    tracker.addStocksVolume("MSFT", 175)
    tracker.addStocksVolume("GOOG", 25)

    # 再次检索
    top_3 = tracker.topKstocks(3)
    print(f"Top 3 stocks after updates: {top_3}")  # GOOG(225), MSFT(175), AAPL(150)