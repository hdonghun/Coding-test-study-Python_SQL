# 출처: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

#1.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        
        
        i=0 
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]: # If not duplicated
                i+=1  # Move i
                nums[i]=nums[j] # Swap
        
        return i+1
        #루프를 벗어나면 자동으로 멈추기 떄문에
        
        
#2. 
#조금 다르게
    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
            
            #포인트 L , M
            # L(인덱스)를 욺직여서....!
            l = 1
            for r in range(1,len(num)):
                if num[r] != num[r-1]:
                   num[l] = num[r]
                   l +=1
            return l





# Time complexity : O(N)

#제자리 정렬(in-place sorting)
# 제자리 정렬을 사용하면 정렬할 대상이 담겨 있는 변수 자체를 정렬된 형태로 바꿔 버립니다. 기존의 정렬되기 전의 모습은 잃게 됩니다.
# 정렬된 결과를 assign할 l-value는 필요 없습니다.


# 강의 영상 참조 : https://www.youtube.com/watch?v=DEJAZBq0FDA
