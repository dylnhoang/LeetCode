class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #graph dfs

        preMap = { i : [] for i in range(numCourses) }

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if preMap[crs] == []:
                return True
            if crs in visited:
                return False

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False #return false if loop detected via visited set
            visited.remove(crs) #done branching from course at this point
            
            preMap[crs] = [] #memoization; if we ever have to explore this again, we'll know it can be finished immediately

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True