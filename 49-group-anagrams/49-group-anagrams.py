class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mapping charCount to list of anagrams
        # list is the value of dict
        # O(m * n)
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] += 1
                # ord arcii code
            
            res[tuple(count)].append(s) # in python, list can't be keys
            
        return res.values()