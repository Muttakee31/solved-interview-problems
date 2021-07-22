def generate(numRows):
        """
        https://leetcode.com/problems/pascals-triangle/
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            triangle = []
            for i in range(numRows+1):
                triangle.append([0 for j in range(i+1)])
            triangle[0] = [1]
            triangle[1] = [1,1]
            for i in range(2, numRows+1):
                for j in range(0, i+1):
                    if j == 0 or j == i:
                        triangle[i][j] = 1
                    else:
                        triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]
                        # .append(triangle[i-1][j-1] + triangle[i-1][j])
        
        # print(triangle)
        return triangle