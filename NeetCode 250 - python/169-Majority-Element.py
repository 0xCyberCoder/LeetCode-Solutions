class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        f = nums[0]
        ans = [1, f]
        for i in range(1, len(nums)):
            if nums[i] == f:
                cnt += 1
                if cnt >= ans[0]:
                    ans[0] = cnt
                    ans[1] = nums[i]
            else:
                f = nums[i]
                cnt = 0
        return ans[1]