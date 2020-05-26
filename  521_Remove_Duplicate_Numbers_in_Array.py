class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        n = len(nums)
        if n == 0 :
            return 0
        nums.sort()
        res = 1 
        for i in range(1, n) :
            if nums[i-1] != nums[i] :
                nums[res] = nums[i]
                res += 1 
        return res 