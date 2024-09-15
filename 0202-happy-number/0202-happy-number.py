class Solution:
    def check(self, no):
        s = 0
        while no:
            s += pow((no % 10), 2)
            no = no//10
        return s

    def isHappy(self, n: int) -> bool:
        s = set()
        s.add(n)
        while n != 1:
            n = self.check(n)
            if n in s:
                return False
            s.add(n)
        return True
        
