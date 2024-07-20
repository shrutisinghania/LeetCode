class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        i = 0
        while (x >= 1 and y >= 4):
            x -= 1
            y -= 4
            i += 1

        if i%2 == 0:
            return "Bob"
        return "Alice"
