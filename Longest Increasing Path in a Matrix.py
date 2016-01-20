class Solution(object):
    def longestIncreasingPath(self, matrix):
        row = len(matrix)
        if not row:
            return 0
        col = len(matrix[0])
        if not col:
            return 0
        graph = [None for i in range(row * col)]
        height = [1 for i in range(row * col)]
        indu = [0 for i in range(row * col)]
        for i in range(row):
            for j in range(col):
                graph[i * col + j] = set()
                if i > 0 and matrix[i][j] < matrix[i - 1][j]:
                    graph[i * col + j].add((i - 1) * col + j)
                    indu[(i - 1) * col + j] += 1
                if i + 1 < row and matrix[i][j] < matrix[i + 1][j]:
                    graph[i * col + j].add((i + 1) * col + j)
                    indu[(i + 1) * col + j] += 1
                if j > 0 and matrix[i][j] < matrix[i][j - 1]:
                    indu[i * col + j - 1] += 1
                    graph[i * col + j].add(i * col + j - 1)
                if j + 1 < col and matrix[i][j] < matrix[i][j + 1]:
                    indu[i * col + j + 1] += 1
                    graph[i * col + j].add(i * col + j + 1)
        #topo get Max height in the map
        queue = []
        maxHeight = 1
        for i in range(row * col):
            if not indu[i]:
                queue.append(i)
        while queue:
            cur = queue.pop(0)
            maxHeight = max(maxHeight, height[cur])
            for neibor in graph[cur]:
                indu[neibor] -= 1
                height[neibor] = max(height[neibor], height[cur] + 1)
                if not indu[neibor]:
                    queue.append(neibor)
        return maxHeight