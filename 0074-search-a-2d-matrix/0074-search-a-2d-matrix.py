class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        Rows,Cols = len(matrix),len(matrix[0])
        top,bottom = 0,Rows-1

        midRow = 0
        while top <= bottom:
            midRow = (top + bottom)//2
            if target < matrix[midRow][0]:
                bottom = midRow - 1
            elif target > matrix[midRow][Cols - 1]:
                top = midRow + 1
            else:
                break

        if not(top <= bottom):
            return False

        l,r = 0,Cols - 1

        while l <= r:
            midCols = (l + r)//2
            if target == matrix[midRow][midCols]:
                return True
            elif target > matrix[midRow][midCols]:
                l = midCols + 1
            else:
                r = midCols - 1
        
        return False