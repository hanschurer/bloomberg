class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Approach 1: 
        (1) Initialize an array "sub" which contains the first element of nums.

        (2) Iterate through the input, starting from the second element. For each element "num":

            If "num" is greater than any element in "sub", then add "num" to "sub".

            Otherwise, iterate through sub and find the first element that is greater than or equal to num. 
            Replace that element with num.

            We have to choose only one element to keep. Well, this is an easy decision, let's take the smaller one since 
            there may be more elements later on that are greater than the smaller one

        (3) Return the length of sub.

        tc: O(N^2) in the worst case. Consider an input where the first half is [1, 2, 3, 4, ..., 99998, 99999], the second half is [99998, 99998, 99998, ..., 99998, 99998]. 
        We would need to iterate (N/2)^2 times for the second half because there are N/2 elements equal to 99998, and a linear scan for each one takes N/2 iterations. 
        This gives a time complexity of O(N^2).

        sc: O(N) When the input is strictly increasing, the sub array will be the same size as the input.
        '''
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than or equal to num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num
        return len(sub)
    
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Approach 2 (improved with binary search): 

        In the previous approach, when we have an element "num" that is not greater than all the elements in "sub", 
        we perform a linear scan to find the first element in "sub" that is greater than or equal to "num". 
        Since "sub" is in sorted order, we can use binary search instead to greatly improve the efficiency of our algorithm.

        In Python, the bisect module provides super handy functions that does binary search for us.

        tc: O(N⋅log(N)) in the worst case. Binary search uses log(N) time as opposed to the O(N) time of a linear scan, which 
        improves our time complexity from O(N^2) to O(N⋅log(N)).

        sc: O(N) When the input is strictly increasing, the sub array will be the same size as the input.
        '''
        from bisect import bisect_left
        sub = []
        for num in nums:
            # ，bisect_left(lst, x)返回lst中大于等于x的第一个下标，bisect(lst, x)和bisect_right(lst, x)返回lst中大于x的第一个元素下标
            i = bisect_left(sub, num) 

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)
    
        
