class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashmap =  Counter(nums)
        res = []

        for i in range(1, len(nums)+1):
            if i not in hashmap:
                res.append(i)
        return res


        