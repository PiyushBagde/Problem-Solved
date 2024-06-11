class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True

        flag = True
        p = nums[0] % 2

        for i in range(1, len(nums)):
            parity = nums[i] % 2

            if parity == p:
                flag = False
                break
            else:
                p = parity
        return flag
        