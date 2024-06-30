class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()                                         # sort the array and use nested loop approach

        for i, n in nums:

            if a > 0: break                                 # Skip +ve integers cuz a no need
            if i > 0 and a == nums[i - 1]:                  # skip if duplicate is detected
                continue
            
            first, last = i + 1, len(nums) - 1              # 2 pointers
            
            while first < last:
                current = a + nums[first] + nums[last]      # Same theory
                if current < 0:
                    first += 1
                elif current > 0:
                    last -= 1
                else:
                    res.append[a + nums[first] + nums[last]]   # add them to results and reupdate the pointers to run the same logic on others

                    #re-update our pointers to fill other arrays in the results list
                    first += 1
                    while first < last and nums[first] == nums[first - 1]: # if left pointer is the same as previous left pointer, 
                                                                           # only need to update one pointer and the other pointer will get update above while loop
                                                                           # to avoid any same output
                        first += 1
        return res
