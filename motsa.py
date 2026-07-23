# Median of Two Sorted Arrays
def findMedianSortedArrays(nums1, nums2):
    l , r = 0, min(len(nums1), len(nums2)) - 1
    total = len(nums1) + len(nums2)
    half = total // 2

    if nums1 > nums2:
        nums1, nums2 = nums2, nums1
            
    while True:
        m = l + (r - l) // 2
        m2 = half - m - 2

        print(m)

        Aleft = nums1[m] if m >= 0 else float("-infinity")
        Aright = nums1[m + 1] if m + 1 < len(nums1) else float("infinity")

        Bleft = nums2[m2] if m2 >= 0 else float("-infinity")
        Bright = nums2[m2 + 1] if m2 + 1 < len(nums2) else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2 == 1:
                return min(Aright, Bright)

            else:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            
        elif Aleft > Bright:
            r = m - 1
            
        else:
            l = m + 1

        