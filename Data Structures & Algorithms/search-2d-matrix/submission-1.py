class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        mSize = m * n
        low = 0
        high = mSize - 1
        while low <= high:
            mid = (low+high)//2
            row = mid // n
            col = mid % n
            if target > matrix[row][col]:
                low = mid + 1
            elif target < matrix[row][col]:
                high = mid - 1
            else:
                return True
            
        return False
        