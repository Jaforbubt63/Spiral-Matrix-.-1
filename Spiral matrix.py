class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        elements = []
        m = len(matrix)
        if m == 0:
            return elements
        n = len(matrix[0])
        
        top, bottom = 0, m-1

        left, right = 0, n-1
        direction = 0
        while len(elements) < m * n:
            if direction == 0:
                for col in range(left, right+1):
                    elements.append(matrix[top][col])
                top += 1
            elif direction == 1:
                for row in range(top, bottom+1):
                    elements.append(matrix[row][right])
                    right -= 1
            elif direction == 2:
                for col in range(right, left-1, -1):
                    elements.append(matrix[bottom][col])
                    bottom -= 1
            else:
                for row in range(bottom, top-1, -1):
                    elements.append(matrix[row][left])
                    left += 1
            direction = (direction + 1) % 4
        
        return elements
        
            