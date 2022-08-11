class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary Search O(nlong(max(p))) O(1)
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            
            if hours <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res