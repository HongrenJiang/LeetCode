class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window O(n) O(1)
        # Move Left step by step
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
#         # Jump Left: Not Straight Forward
#         HashMap = {} # Char -> Index
#         res = 0
#         l = 0
        
#         for r in range(len(s)):
#             if s[r] in HashMap:
#                 l = max(HashMap[s[r]] + 1, l) # remove left to the right of old r to avoid repeating
#                 # why it can't be l = HashMap[s[r]]
#                 # because HashMap doesn't remove the element out of the window
#             res = max(res, r - l + 1)
#             HashMap[s[r]] = r # update the index

#         return res