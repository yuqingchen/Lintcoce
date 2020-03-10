from collections import deque
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        # write your code here
        queue = deque([s])
        visit = set([s])
        minlen = len(s)
        while queue :
            node = queue.popleft()
            for sub in dict :
                found = node.find(sub)
                while found != -1 :
                    newstr = node[:found] + node[found + len(sub) :]
                    if newstr not in visit :
                        if len(newstr) < minlen :
                            minlen = len(newstr)
                        visit.add(newstr)
                        queue.append(newstr)
                    found = node.find(sub, found + 1)
        return minlen