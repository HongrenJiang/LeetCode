class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # binary tree + depth first search
        res = []
        
        def dfs(i, curr, total):
            if total == target:
                # Note this part -- 1
                res.append(curr.copy())
                print(res)
                return
            if total > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        
        return res
# If I append curr
# the next time the if the curr is modified, 
# the old curr which has already been append is also modified
# I think it's because what I added into res 
# is a pointer to curr list
# so if I changed the curr later, the curr in the res list will be
# also changed
# Do use curr.copy()