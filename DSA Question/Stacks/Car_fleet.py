class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # this is list comprehension it will  become pair car_pos, speed
        # pair = [(10, 2), (8, 4), (0, 1), (5, 1), (3, 3)]  
        pair = [(p, s) for p, s in zip(position, speed)]
        
        # use sort
        pair.sort(reverse=True)
        stack = [] # intialize stack

        for p, s in pair:  # run iteration
            # append the calculations of car to reach the target
            stack.append((target - p) / s)

            # if the time at the top car at the top-stack using -1 is less than 2nd top car on the stack means both has collided 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # then pop to decrease the no. of car fleets
                stack.pop()
            #Important why we didn't use while instead of IF, to make sure when both car collides they they both counted and pop, unlike in while where 
            # the 2nd car that has already collided with 1st, get collided again with 3rd one, that doesn't make sense.
            # In short to keep it simple and less complex use IF in this case makes more sense
        return len(stack)
