# 출처: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        for i in range(0, len(nums)):
            if nums[i] != val :
                nums[k] = nums[i] 
                k += 1
                
        return k


# 공부 영상 : https://www.youtube.com/watch?v=Pcd1ii9P9ZI

# 신기하게 방법이 똑같다 ㅎㅎ


