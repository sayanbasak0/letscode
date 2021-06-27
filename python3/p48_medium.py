## 48. Rotate Image
## https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)-1):
            for j in range(i,len(matrix[i])-1-i):
                matrix[i][j],matrix[len(matrix)-1-j][i],matrix[len(matrix)-1-i][len(matrix)-1-j],matrix[j][len(matrix)-1-i] = matrix[len(matrix)-1-j][i],matrix[len(matrix)-1-i][len(matrix)-1-j],matrix[j][len(matrix)-1-i],matrix[i][j]
                # matrix[i][j] = matrix[len(matrix)-1-j][i]
                # matrix[len(matrix)-1-j][i] = matrix[len(matrix)-1-i][len(matrix)-1-j]
                # matrix[len(matrix)-1-i][len(matrix)-1-j] = matrix[j][len(matrix)-1-i]
                # matrix[j][len(matrix)-1-i] = matrix[i][j]