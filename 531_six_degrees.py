from collections import deque

class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        # write your code here
        queue = deque([s])
        visited = set([s])
        level = 0
        while queue :
            level += 1 
            for i in range(len(queue)) :
                node = queue.popleft()
                if node == t :
                    return level - 1 
                for neighbor in node.neighbors :
                    if neighbor not in visited :
                        visited.add(neighbor)
                        queue.append(neighbor)
        return -1