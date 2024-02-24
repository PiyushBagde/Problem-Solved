class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lst  = list(s.split())
        ans = lst[:k]
        return " ".join(ans)
        