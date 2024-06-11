class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True

        p = nums[0] % 2

        for i in range(1, len(nums)):
            parity = nums[i] % 2

            if parity == p:
                return False
            else:
                p = parity
        return True
        