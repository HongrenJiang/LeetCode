class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding Window O(n) O(1)
        if len(s1) > len(s2):
            return False
        
        count1 = {} # char -> count
        count2 = {}
        l = 0
        
        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)
        
        # print(count1)
            
        for i in range(len(s1)):
            count2[s2[i]] = 1 + count2.get(s2[i], 0)
        
        while l + len(s1) - 1 < len(s2):
            # print(count2)
            if count1 == count2:
                return True
            
            count2[s2[l]] -= 1
            if(count2[s2[l]] == 0):
                del count2[s2[l]]
            
            if l + len(s1) < len(s2):
                count2[s2[l + len(s1)]] = 1 + count2.get(s2[l + len(s1)], 0)
            l += 1
        
        return False  