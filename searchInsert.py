class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return nums.index(lambda x: x > target)
        for x in nums:
            if x >= target:
                return nums.index(x)
        else:
            return len(nums)
print(Solution().searchInsert( [1,3,5,6], 7))
