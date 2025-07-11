class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < numRows or numRows == 1:
            return s

        rows = [[] for row in range(numRows)]

        row_index, direction = 0, 1

        for char in s:
            rows[row_index].append(char)

            if row_index == 0:
                direction = 1
            if row_index == numRows - 1:
                direction = -1
            
            row_index += direction
        
        for i in range(numRows):
            rows[i] = "".join(rows[i])
        
        return "".join(rows)
