class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A :
            return [-1, -1]
        start, end = 0, len(A) - 1 
        left = 0
        while start + 1 < end :
            mid = (start + end) // 2 
            if A[mid] < target :
                start = mid 
            else :
                end = mid 
        if A[start] == target :
            left = start 
        elif A[end] == target :
            left = end 
        else :
            left = -1
        start, end = left, len(A) - 1 
        right = 0
        while start + 1 < end :
            mid = (start + end) // 2 
            if A[mid] <= target :
                start = mid 
            else :
                end = mid 
        if A[end] == target :
            right = end 
        elif A[start] == target :
            right = start
        else :
            right = -1 
        return [left, right]