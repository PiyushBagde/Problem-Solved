class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        prod = 1
        count = 0
        while right < len(nums):
            prod *= nums[right]

            while prod >= k  and left <= right:
                prod = prod // nums[left]
                left += 1

            count += right-left + 1
            right += 1
        return count

        