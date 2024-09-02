class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        same = 1
        i = 1
        if nums[0] == nums[-1] or len(nums) == 2:
            return 2

        while nums[i] - nums[i-1] >= 0:
            if nums[i] == 1*(10**4)+1:
                    return i
            if nums[i] - nums[i-1] == 0:
                same += 1
                if same > 2:
                    nums.pop(i)
                    if nums[-1] != 1*(10**4)+1:
                        nums.append(1*(10**4)+1)
                    same -= 1
                    if nums[i] == 1*(10**4)+1:
                        return i
                    continue
            else:
                same = 1
            
            i += 1

            if i >= len(nums):
                return i
        return i - 1

        