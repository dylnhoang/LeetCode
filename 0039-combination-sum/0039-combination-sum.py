class Solution(object):
    def combinationSum(self, candidates, target):
        res = [] #use array for global modification in recursive method

        def dfs(i, cur, total): #current idx of candidates, current array, total sum of array
            if total == target:
                res.append(cur.copy()) #we use a copy because we are passing in cur later, and don't want it to change later
                return
            elif total >= target or i >= len(candidates): #if total is more than target or we've visited all candidates in list
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i]) #continue exploring the left path (adding left-most element)
            cur.pop()
            dfs(i + 1, cur, total) #explore the right path (adding righter element)
        
        dfs(0, [], 0) 
        return res