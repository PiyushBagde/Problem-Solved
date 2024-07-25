class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = Counter(nums1)
        dict2 = Counter(nums2)
        lst = []

        for i in dict1:
            if i in dict2:
                lst.extend([i] * (min(dict1[i], dict2[i])))
            
        return lst

        