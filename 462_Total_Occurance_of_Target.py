class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        if not A :
            return 0
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
        start, end = 0, len(A) - 1 
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
        if left == -1 or right == -1 :
            return 0
        return right - left + 1