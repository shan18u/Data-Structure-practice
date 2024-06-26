class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # Step 1: we need a list of [1]'s similar size to the nums

        for i in range(1, len(nums)):       # start from index 1 cuz we need a prefix to start calculates
            res[i] = res[i-1] * nums[i-1]   # calculate and then assign it to res and use previous multipled portion to calculate forward until loop ends
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):   # reverse
            res[i] *= postfix                  # check doc for examples
            postfix *= nums[i]                 # postfix * and update the result
        return res

            