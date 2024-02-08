class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum([1 if op == '++X' or op == 'X++' else -1 for op in operations])
            