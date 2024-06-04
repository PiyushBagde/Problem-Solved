class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        j = 1
        flag = 0

        while j < len(nums):
            if flag == 0 and nums[i] > nums[j]:
                flag = 1
                if nums[0] < nums[j]:
                    return False
            elif flag == 1:
                if nums[i] > nums[j] or nums[0] < nums[j]:
                    return False
            i = j
            j += 1
        return True
            