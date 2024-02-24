class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        s = len(nums)
        for i in range(s):
            if i == 0:
                left = 0
            else:
                left = sum(nums[:i])
            if i == s-1:
                right = 0
            else:
                right = sum(nums[i+1:])
            ans.extend([abs(left-right)])
        return ans

                    