class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]: # if the middle value is == target then just return mid
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]: 
                
                if target > nums[mid] or target < nums[l]:  # Checks if we have to move serach in right section or not
                # For example [4, 5, 6, 7, 0, 1, 2] -> target = 0. 1st iteration: mid = 7
                # if target in less than mid -> 0 < 7 OR target is less than left-most number in the search 
                # we know that the trget then must be in the right section cuz remember 
                # the array if halfly sorted 4, 5, 6, 7 
                    l = mid + 1   # move the search to right section
                else:
                    r = mid - 1  # else means mid is < left, hence we are in right sorted array 
            
            # right sorted portion
            else:
                
                if target < nums[mid] or target > nums[r]: # same checks if we have to move search in left section or not, only if t < mid OR t > right most number in that search
                    r = mid - 1
                else:
                    l = mid + 1
        
        
        return -1
