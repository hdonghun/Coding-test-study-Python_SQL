# 출처: https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        k = 0
        
        for i in range(0,len(nums)):
            if nums[i] < target:
                k += 1
        
            if nums[i] == target:
                break;
        return k

# 다른 사람이 푼 방법
# 출처: https://www.youtube.com/watch?v=K-RYzDZkzCI&t=664s
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
# Log(n)
l, r = 0, len(nums)- 1

while l <= r:
    mid = (1+r) // 2

    if target == nums[mid]:
        return mid
    if target > nums[mid]:
        l = mid + 1
    else:
        r = mid -1

return l




