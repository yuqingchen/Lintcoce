class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        start, end = 0, len(A) - 1 
        while start + 1 < end :
            mid = (start + end) // 2 
            if A[mid] <= target :
                start = mid 
            else :
                end = mid
        if target - A[start] <= A[end] - target :
            return start
        else :
            return end