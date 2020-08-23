class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        res = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0
        return max(res, count)