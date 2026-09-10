class Solution(object):
    def getRow(self, rowIndex):
        previous = []
        for i in range(rowIndex + 1):
            row = [1]
            if i > 0:
                for j in range(1,len(previous)):
                    row.append(previous[j] + previous[j-1])

                row.append(1)
            
            previous = row
        
        return row