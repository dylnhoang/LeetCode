class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #cycle detection

        adjMap = { i : [] for i in range(n) }

        for t, f in edges:
            adjMap[t].append(f)
            adjMap[f].append(t)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for edge in adjMap[node]:
                if edge == parent:
                    continue
                if not dfs(edge, node):
                    return False
            
            return True

        if not dfs(0, -1):
            return False

        return n == len(visited) #all nodes are visited, ensures connectivity