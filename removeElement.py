class Solution:
    def removeElement(self, nums, val):
        index = 0
        for i in range(len(nums)):
            if(nums[i]!=val):
                nums[index] = nums[i]
                index+=1
        return nums

print(Solution().removeElement([1,3,4,2,3,2,4,4], 2))