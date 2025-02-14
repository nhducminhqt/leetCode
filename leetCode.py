import heapq
class Solution(object):
    def minOperations(self, nums, k):
        res = 0
        heapq.heapify(nums)
        while nums[0] < k:
            min_f = heapq.heappop(nums)
            min_s = heapq.heappop(nums)
            sum_two_min = min(min_f,min_s)*2+max(min_f,min_s)
            heapq.heappush(nums,sum_two_min)
            res+=1
        return res