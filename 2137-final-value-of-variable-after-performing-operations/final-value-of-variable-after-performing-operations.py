class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = [1 if op in ["++X",  "X++"] else -1 for op in operations]
        return sum(ans)
        