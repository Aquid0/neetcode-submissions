class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            mid = (l + r) // 2 
            rowIndex = mid // n
            colIndex = mid % n

            if matrix[rowIndex][colIndex] == target:
                return True
            elif matrix[rowIndex][colIndex] < target:
                l = mid + 1
            else: 
                r = mid - 1
        
        return False
            
