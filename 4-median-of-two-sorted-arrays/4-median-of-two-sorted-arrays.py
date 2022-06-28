class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if(len(A) > len(B)):
            A, B = B, A
        total = len(A) + len(B)
        half = total // 2 # half of the total (even) or (half -1) of the total (odd)
        l, r = 0, len(A) -1 # binary search index
        
        while True:
            i = (l + r) // 2 # median index of binary search (or the left one)
            j = half - i - 2
            # (i + 1): how many numbers in the left partition of A
            # half - (i + 1) how many numbers in the left partition of B
            # half - (i + 1) -1 transfer it into index
            # j = half - i - 2
            
            leftA = A[i] if i >= 0 else float("-infinity")
            rightA = A[i + 1] if (i + 1) < len(A) else float("infinity")
            leftB = B[j] if j >= 0 else float("-infinity")
            rightB = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            if leftA <= rightB and leftB <= rightA:
                if total % 2:
                    #odd
                    return min(rightA, rightB)
                else:
                    #even
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1