class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = 0 
        j = 1
        res = [0] * len(nums)

        for k in range(len(nums)): # time complexity O(n)
            if nums[k] >= 0:
                res[i] = nums[k]
                i += 2
            else:
                res[j] = nums[k]
                j += 2

        # space complexity O(n)
        return res




        