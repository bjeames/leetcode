class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        counter = 0
        visited = set()

        def dfs(i):
            visited.add(i)
            for nei in adj[i]: 
                if nei not in visited:
                    dfs(nei)
            return
    
        for i in range(n):
            if i not in visited:
                counter+=1
                dfs(i)

        return counter
    

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            return

        counter = 0
        for i in range(n):
            if i not in visited:
                counter+=1
            dfs(i)

        return counter
        


        

