class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sum_m = sum(rolls)
        sum_n = (mean * (m + n)) - sum_m
        p = sum_n / n
        if 1 > p or p  > 6:
            return []
        avg_n = sum_n // n 
        rem = sum_n % n
        if rem == 0:
            return [avg_n] * n
        l = [avg_n] * (n - rem)
        rem_l = [avg_n + 1] * rem
        return l + rem_l
         
        