class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r_index = 0
        l_index = 0
        res = []
        if nums[0] >= 0:
            return [i**2 for i in nums]
        elif nums[-1] < 0:
            return [i**2 for i in nums[::-1]]
        else:
            for k in range(len(nums)):
                if nums[k] >= 0:
                    r_index = k
                    l_index = k - 1
                    break
            
        while l_index >= 0 and r_index < len(nums):
            left_val = nums[l_index]**2
            right_val = nums[r_index]**2

            if left_val  > right_val:
                res.append(right_val)
                r_index += 1

            elif left_val < right_val:
                res.append(left_val)
                l_index -= 1

            else:
                res.append(left_val)
                res.append(right_val)

                l_index -= 1
                r_index += 1

        while r_index < len(nums):
            res.append(nums[r_index]**2)
            r_index += 1
        while l_index >= 0:
            res.append(nums[l_index]**2)
            l_index -= 1

            

            
        return res

            

        


