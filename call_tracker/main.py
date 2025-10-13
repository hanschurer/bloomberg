# 写一个class只有一个method 如果这个class在过去3秒内被call了more than 3 times return True不然return False

# https://www.1point3acres.com/bbs/thread-1100830-1-1.html
import time

class CallTracker:
    def __init__(self):
        # 存储每次调用的时间戳
        self.call_timestamps = []
    
    def is_over_limit(self):
        """
        检查过去3秒内调用次数是否超过3次
        返回True如果超过，否则返回False
        """
        current_time = time.time()
        # 记录当前调用时间
        self.call_timestamps.append(current_time)
        
        # 移除3秒前的调用记录
        # 找到第一个在3秒内的时间戳索引
        cutoff_time = current_time - 3
        # 从列表开头移除所有超过3秒的时间戳
        while self.call_timestamps and self.call_timestamps[0] < cutoff_time:
            self.call_timestamps.pop(0)
        
        # 判断过去3秒内的调用次数是否超过3次
        return len(self.call_timestamps) > 3
