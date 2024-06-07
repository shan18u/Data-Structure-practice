class Solution:
    def minEatingSpeed(self, banana_piles: List[int], hours_available: int) -> int: # h = hours_available 
        left, right = 1, max(banana_piles) # maximum no. in the piles
        minimum_speed = right  # cuz we need the slowest acceptable speed

        while left <= right:
            current_speed = (left + right) // 2

            total_hours_needed = 0
            for pile in banana_piles:  # loop through all the pile

                total_hours_needed += math.ceil(float(pile) / current_speed)  # calculation get round up using .ceil, if ans 5.5 its 6

            if total_hours_needed <= hours_available: 
                minimum_speed = current_speed   # update the result to current speed
                right = current_speed - 1 # and then decrease the right pointer to check for better result
            else:
                left = current_speed + 1 # vice versa
        return minimum_speed
