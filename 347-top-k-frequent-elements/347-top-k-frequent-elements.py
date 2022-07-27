class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        hashMap = { } # num -> count
        
        for i, num in enumerate(nums):
            hashMap[num] = 1 + hashMap.get(num, 0)
        
        # return heapq.nlargest(k, hashMap.keys(), key = hashMap.get)
        # heqpq.nlargest is an advanced function, let's show its process
        
        # freq: count -> num
        # freq[c] will store the num which appears c times, 
        # and it's automatically so
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in hashMap.items():
            freq[count].append(num)
        
        # Take the highest k frequency nums
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
        
        