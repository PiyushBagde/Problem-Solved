class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        dict1 = {}
        count = 0

        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
            
        for i in nums:
            if i+k in dict1:
                count  = count + dict1[i+k]
        return count
        