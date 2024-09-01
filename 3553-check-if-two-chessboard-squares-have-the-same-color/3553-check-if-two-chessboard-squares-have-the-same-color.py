class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        b = [1, 3, 5, 7]
        c1 = ord(coordinate1[0]) - ord('a')
        r1 = int(coordinate1[1])
        c2 = ord(coordinate2[0]) - ord('a')
        r2 = int(coordinate2[1])
        col1, col2 = -1, -1
        for j in b:
            if r1 == j:
                col1 = 1
            if r2 == j:
                col2 = 1
        for i in range(c1):
            col1 *= -1
        for i in range(c2):
            col2 *= -1
        return col1 == col2
            
