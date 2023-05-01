class Solution:
    def average(self, salary: List[int]) -> float:
        mi = min(salary)
        ma = max(salary)
        s = sum(salary)
        return (s - mi - ma) / (len(salary) - 2)