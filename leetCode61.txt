class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l=set()
        j=0
        n=len(nums)
        for i in range(n):
            if nums[i]==key:
                if i-k>=0:
                    j=i-k
                while j<i+k+1 and j<n:
                    l.add(j)
                    j+=1
        l=list(l)
        return l
        