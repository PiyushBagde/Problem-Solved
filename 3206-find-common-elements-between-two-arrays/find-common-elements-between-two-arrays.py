class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = set(nums1)
        dict2 = set(nums2)
        count1 = 0
        count2 = 0

        for i in nums1:
            if i in dict2:
                count1 += 1
        for i in nums2:
            if i in dict1:
                count2 += 1

        return [count1, count2]

