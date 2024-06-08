class Solution:

# in the rotated array the number in most cases end up on the opposite side like [1,2,3,4,5] -> [1,4,4,2,5]
# which tells us that the lower or smaller number ends up on the right side and bigger on the left side, which is usually opposite in non-rotated arrays


    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # 1st number in array gets assign to result, will be change later 

        l, r = 0, len(nums) - 1
        while l <= r:

            if nums[l] < nums[r]: # 1st part check to see is the array in sorted and or l < r 
                res = min(res, nums[l])   # assign the minimum no. to the result
                break                       # break out of loop
            
            m = (l + r) // 2
            res = min(res, nums[m])  # update the result

            if nums[m] >= nums[l]:  # check if mid value is part of left sorted portion, yes, then go to right
                l = m + 1
            else:
                r = m - 1
        return res

