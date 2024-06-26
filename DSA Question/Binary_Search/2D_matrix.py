class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, cols = len(matrix), len(matrix[0]) # why[0] cuz to start search from the last column
        top, bot = 0 , row -1 # why -1 cuz to start search from the last row

    #will need 2 binary searches, 1st to search the row
        while top <= bot: 
            row_mid = (top + bot) // 2
            if target > matrix [row_mid][-1]: # why -1 cuz to start from the rightmost biggest number in that row
                top = row_mid + 1 # cuz if t=6 and rowbiggest no. is 5, that means we go up to smaller no. of rows 
            elif target < matrix[row_mid][0]: # 0 to start from the leftmost smallest no. in given row
                bot = row_mid - 1 #vice-versa
            else: break
        
        if not (top <= bot): return False #target not found 

        row_mid = (top + bot) // 2 #re-initialize

        # 2nd is to search the columns
        l, r = 0 , cols - 1
        while l <= r:
            m = (l + r) // 2

            if target > matrix[row][m]: # why m cuz to start from mid to the chosen side
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else: return True
    
        return False
