class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx = -1
        m = len(matrix)
        n = len(matrix[0])
        for i in range(0, m):
            if target < matrix[i][n-1]:
                idx = i
                break
            if target == matrix[i][n-1]:
                return True
        if idx == -1:
            return False
        
        l = 0
        h = n - 1
        while l <= h:
            m = (l+h)//2
            if target > matrix[idx][m]:
                l = m + 1
            elif target < matrix[idx][m]:
                h = m - 1
            else:
                return True
        return False
        