class Solution:
    def removeDuplicates(self, nums):
        index = 1
        for i in range(1,len(nums)):
            if(nums[i-1]!=nums[i]):
                nums[index] = nums[i]
                index+=1
        return nums

print(Solution().removeDuplicates([1,2,2,2,3,4,4,4]))