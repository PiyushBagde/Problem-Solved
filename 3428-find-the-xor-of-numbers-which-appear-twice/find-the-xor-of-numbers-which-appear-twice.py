class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        hashmap = {}
        res = []

        for i in nums:
            if i in hashmap:
                res.append(i)
            else:
                hashmap[i] = i
        if len(res)==0:
            return 0
        for i in range(1,len(res)):
            res[0] = res[0] ^ res[i]

        return res[0]