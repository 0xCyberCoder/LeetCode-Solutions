class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = 101
                count += 1

        
        nums.sort()
        return len(nums) - count

            