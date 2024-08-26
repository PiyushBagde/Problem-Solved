class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        hashmap = {}
        res = []
        twice = False

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
            
        for key, value in hashmap.items():
            if value == 2:
                twice = True
                res.append(key)
        if twice:
            for i in range(1, len(res)):
                res[0] = res[0] ^ res[i]
            return res[0]
            
        return 0
        