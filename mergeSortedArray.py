class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(1, len(nums1) + 1):
            if i > m:
                for j in range(0, len(nums2)):
                    nums1[(i - 1) + j] = nums2[j]
                break
        nums1.sort()
                    