class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        
        Args:
            nums: list[int]
        """
        # [0, j) < 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # if j != i:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        