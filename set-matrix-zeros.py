class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rset = set()
        cset = set()
        #storing the rows and cols that need to be made 0
        for i in range(rows) :
            for j in range(cols) :
                if matrix[i][j]==0 :
                    rset.add(i)
                    cset.add(j)

        for i in rset :
            for j in range(cols) :
                matrix[i][j] = 0
        
        for i in range(rows) :
            for j in cset :
                matrix[i][j] = 0

        return matrix
