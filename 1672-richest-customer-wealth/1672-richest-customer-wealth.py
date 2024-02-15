class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        accounts = [sum(i) for i in accounts]
        return max(accounts)
        