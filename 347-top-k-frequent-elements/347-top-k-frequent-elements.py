class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = { } # num -> count
        
        for i, num in enumerate(nums):
            hashMap[num] = 1 + hashMap.get(num, 0)
        
        return heapq.nlargest(k, hashMap.keys(), key = hashMap.get)
        