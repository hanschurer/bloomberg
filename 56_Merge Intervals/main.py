# — Title: Merge Maintenance Windows
# Difficulty: Medium
# Prompt: Given a list of market data maintenance windows (time intervals) on trading servers, merge all overlapping intervals and return the consolidated schedule.

class Solution:
    def merge(self, intervals):
        #sort intervals by the start value
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            last = result[-1]
            current = intervals[i]
            #if overlapping, merge them
            if last[1] >= current[0]:
                last[1] = max(last[1], current[1])
            else:
                result.append(current)

        return result
