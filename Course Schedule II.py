class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def __init__(self):
        self.topo=[]
    def dfs_connect(self,graph,visited,startnode):
        visited[startnode]=1
        if graph[startnode]:
            for neibor in graph[startnode]:
                if visited[neibor]==1:
                    return False
                elif not visited[neibor]:
                    if not self.dfs_connect(graph,visited,neibor):
                        return False
        visited[startnode]=2
        self.topo.append(startnode)
        return True
    def dfs(self,numCourses,graph):
        visited=[0 for i in range(numCourses)]
        for i in range(numCourses):
            if not visited[i]:
                if not self.dfs_connect(graph,visited,i):
                    return False
        return True
    def findOrder(self, numCourses, prerequisites):
        graph={}.fromkeys(range(numCourses),None)
        for j,i in prerequisites:
            if not graph[i]:
                graph[i]=[]
            graph[i].append(j)
        return self.topo[::-1] if self.dfs(numCourses,graph) else []