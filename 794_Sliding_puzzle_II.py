from collections import deque
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        # # write your code here
        start, end = "", ""
        for i in range(3) :
            for j in range(3) :
                start += str(init_state[i][j])
                end += str(final_state[i][j])
        queue = deque([start])
        visited = set([start])
        dist = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        level = 0
        while queue :
            #print(queue)
            for i in range(len(queue)) :
                node = queue.popleft()
                if node == end :
                    return level
                pos = node.find('0')
                x, y = pos//3, pos%3
                for dx, dy in dist :
                    nx = x + dx
                    ny = y + dy
                    if(nx < 0 or nx >= 3 or ny < 0 or ny >= 3) :
                        continue 
                    npos = 3*nx + ny
                    a, b = max(npos, pos), min(npos, pos)
                    newnode = node[0:b] + node[a] + node[b + 1:a] + node[b] + node[a + 1:]
                    if newnode not in visited :
                        visited.add(newnode)
                        queue.append(newnode)
            level += 1 
        return -1