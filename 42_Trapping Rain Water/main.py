from typing import List


class Solution:
    '''
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
               idx
               l_most
                                   r_most
    l_most = r_most = 1
    At idx, water captured = max(0, min(l_most, r_most) - height[idx])
    '''
    def trap(self, height: List[int]) -> int:
        l_most = r_most = l = res = 0
        r = len(height) - 1
        while l <= r:
            if height[l] < height[r]:
                l_most = max(l_most, height[l])
                res += l_most - height[l]
                l += 1
            else:
                r_most = max(r_most, height[r])
                res += r_most - height[r]
                r -= 1
        return res
