class Solution:
    def combinationSum4(self, nums, target):
        """
        Args:
            nums: list[int]
            target: int
        
        Return:
            int
        """
        nums.sort()
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i - num]
        return dp[-1]
