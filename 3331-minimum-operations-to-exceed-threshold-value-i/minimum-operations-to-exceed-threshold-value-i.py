class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        opr = 0
        for num in nums:
            if num<k:
                opr += 1
        return opr
        