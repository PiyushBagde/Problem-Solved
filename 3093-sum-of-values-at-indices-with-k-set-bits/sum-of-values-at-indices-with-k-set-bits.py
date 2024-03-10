class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        s = len(nums)
        for i in range(s):
            if bin(i)[2:].count('1') == k:
                res = res + nums[i]
        return res

        