class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = [0] * n 
        on_path = [False] * n
        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())  
                return
            for j, on in enumerate(on_path):
                if not on:
                    path[i] = nums[j]  
                    on_path[j] = True  
                    dfs(i + 1)
                    on_path[j] = False  
                  
        dfs(0)
        return ans

#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
