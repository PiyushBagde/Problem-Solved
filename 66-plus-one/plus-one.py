class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        sm = 0

        for i in digits:
            sm = sm*10 + i

        sm += 1

        return [int(n) for n in str(sm)]
        