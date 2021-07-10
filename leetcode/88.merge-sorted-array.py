class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        needed help writing the conditions of if cases.
        """
        last = m+n-1
        i, j = m-1, n-1

        while last>=0:
            if j<0 or (i>=0 and nums1[i]>=nums2[j]):
                nums1[last]=nums1[i]
                i-=1
            else:
                nums1[last]=nums2[j]
                j-=1
            last-=1
