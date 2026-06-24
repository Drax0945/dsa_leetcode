class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        if len(nums1)>len(nums2):
            A, B = B, A #A is the shorter array

        a, b = len(A), len(B)

        full_len = a+b
        half_len = int((a+b+1)/2)

        l, h = 0, a

        

        while True:

            part_a = (l+h)/2
            part_b = half_len - part_a    

            A_left  = A[part_a - 1] if part_a > 0 else float("-infinity")
            A_right = A[part_a] if part_a < a else float("infinity")
            B_left  = B[part_b - 1] if part_b > 0 else float("-infinity")
            B_right = B[part_b] if part_b < b else float("infinity")

            if A_left <= B_right and B_left <= A_right:
                if full_len%2!=0:
                    med = max(A_left, B_left)
                    return med
                med = (max(A_left, B_left) + min(A_right, B_right))/2.0
                return med
            elif A_left > B_right:
                h = part_a - 1
            else:
                l = part_a + 1    
            



        