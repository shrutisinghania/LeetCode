class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        a = 0
        p = 0
        for i in bank:
            c = i.count('1')
            if c != 0:
                if p!=0:
                    a += p*c
                p = c
        return a