class Solution(object):
    def generate(self, numRows):
        triangle = []

        for i in range(numRows):
            row = [1]

            if i > 0:
                previous = triangle[i-1]
                for j in range(1,len(previous)):
                    row.append(previous[j] + previous[j-1])

                row.append(1)

            triangle.append(row)

        return triangle