class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L :
            return 0
        start, end = 1, max(L)
        while start + 1 < end :
            length = (start + end) // 2 
            if self.get_pieces(L, length) >= k :
                start = length 
            else :
                end = length
        if self.get_pieces(L, start) >= k :
            return start 
        if self.get_pieces(L, end) >= k :
            return end 
        return 0
            
    def get_pieces(self, L, length) :
        pieces = 0
        for l in L :
            pieces += l // length
        return pieces