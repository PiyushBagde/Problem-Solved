class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Brute force
        pos = []
        neg = []
        res = []

        for i in nums:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)

        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res
        
        