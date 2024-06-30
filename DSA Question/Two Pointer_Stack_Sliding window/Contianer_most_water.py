class Solution:
    def maxArea(self, height: List[int]) -> int:
        # HINT: max_area =  height * weight
        
        # init 2 pointers and current area 
        max_area = 0 
        first = 0
        last = len(height) - 1

        while first < last:
            curr_height = min(height[first], height[last])  # min_area is the lowest value between both current pointers
            curr_width = last - first
            curr_area = curr_height * curr_width

            max_area = max(curr_area, max_area)             # max_area is just to updating the maximum area by comparing new to older area

            if height[first] > height[last]:                # if 1st_pointer > 2nd, then we need to move left to right 
                last -= 1
            else:                                           # why cuz we need to find biggest bar from both sides
                first += 1                                  # else prefer the right bar
        return max_area