class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        s = len(nums)
        target = []
        for i in range(s):
            target.insert(index[i], nums[i])
        return target
        