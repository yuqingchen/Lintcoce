class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if len(pages) == 0 :
            return 0
        left, right = max(pages), sum(pages)
        while left + 1 < right :
            mid = (left + right) // 2 
            if self.check(pages, k, mid) <= k :
                right = mid 
            else :
                left = mid 
        if self.check(pages, k, left) <= k :
            return left
        else :
            return right 
                
    def check(self, pages, k, mid) :
        num = 1 
        pagesum = 0
        for page in pages :
            if pagesum + page <= mid :
                pagesum += page 
            else :
                num += 1 
                pagesum = page 
        return num