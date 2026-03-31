class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one, two = m-1, n-1
        idx = m+n-1

        while one >= 0 and two >= 0:
            if nums1[one] >= nums2[two]:
                nums1[idx] = nums1[one]
                one -= 1
            else:
                nums1[idx] = nums2[two]
                two -= 1
            idx -= 1
        while two >= 0:
            nums1[idx] = nums2[two]
            two -= 1
            idx -= 1
        