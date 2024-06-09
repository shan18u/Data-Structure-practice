class Solution:
    #LEETCODE 4
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2 # assign 2 given array to variables
        total = len(nums1) + len(nums2) # total length of both arrays 
        half = total // 2   # half of total, and it will tell us the total elements we have in the left partition 

        if len(B) < len(A): # In order to make sure that Array (A) is smaller than (B), we will check condition if yes, we will swap the arrays to get a smaller A and larger B
            A, B = B, A
        
        l, r = 0, len(A) - 1   #pointers

        while True:
            i = (l + r) // 2  # middle value to split A
            j = half - i - 2  # middle value to split B, based on i and the total number of elements from both arrays

            # To be able to compare and see if we got our median right or calculate those potential splits, will need these values   
            # Also, add if-else to make sure that we don't go out of bounds, add ..infinity.. (default value)
            Aleft = A[i] if i >= 0 else float("-infinity") 
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")

            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # logic
            if Aleft <= Bright and Bleft <= Aright: # check if our left-partition is correct?
                
                # check if odd
                if total % 2: 
                    return min(Aright, Bright) # for ex. min(2, inifinity) -> 2
                # check if even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 # get median in this case by dividing, check doc
            
            elif Aleft > Bright: # if we don't find any median, then too many left in (A), then need to decrease the size from (A)
                r = i - 1
            
            else: # increase (A)
                l = i + 1
