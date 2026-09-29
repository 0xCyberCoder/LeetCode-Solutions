class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = 0
        y = 0
        res = []
        while x < m and y < n:
            if nums1[x] < nums2[y]:
                res.append(nums1[x])
                x += 1
            else:
                res.append(nums2[y])
                y += 1

        while x < m:
            res.append(nums1[x])
            x += 1

        while y < n:
            res.append(nums2[y])
            y += 1

        nums1[:] = res[:]
        