class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for i in range(0, len(nums)):
            if nums[i] == val:
                nums[i] = 55
                cnt += 1

        nums.sort()
        return len(nums) - cnt