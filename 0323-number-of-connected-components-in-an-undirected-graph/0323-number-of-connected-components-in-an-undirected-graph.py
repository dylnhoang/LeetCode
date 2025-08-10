class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = { i : [] for i in range(n) }

        for t, f in edges:
            adjMap[t].append(f)
            adjMap[f].append(t)
        
        visited = set()
        components = 0

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for cnct in adjMap[node]:
                dfs(cnct)

            return True

        for i in range(n):
            if dfs(i):
                components += 1

        return components