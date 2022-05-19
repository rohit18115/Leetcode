class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mat_new = []

        for j in range(len(mat)):
            k = j
            i = 0
            temp = []
            while k >= 0:
                temp.append(mat[i][k])
                i += 1
                k -= 1
            if j % 2 == 0:
                temp.reverse()
            mat_new.extend(temp)
        for i in range(1, len(mat)):
            j = len(mat) - 1
            k = i
            temp = []
            while k < len(mat):
                print(i, j, k)
                temp.append(mat[k][j])
                k += 1
                j -= 1
            if i % 2 == 0:
                temp.reverse()
            mat_new.extend(temp)
        return mat_new
