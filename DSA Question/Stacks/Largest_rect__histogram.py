class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # this list will store pairs of both index and its height

        # run loop with both i and height
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # if top value height in stack is greater than the height we just reached
                index, height = stack.pop()    # then pop both i and h
                maxArea = max(maxArea, height * (i - index)) # check max rectangle we can create and extend the current height backwards
                start = index # now we can extend start index backwards
            stack.append((start, h)) # add pair start index (the index that we pushed all the way back) and height

        for i, h in stack: # now we will compute the height of extended at the end of histogram then, update max area 
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
