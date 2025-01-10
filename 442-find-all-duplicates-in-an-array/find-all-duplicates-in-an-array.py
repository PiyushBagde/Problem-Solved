class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        num_visited = set()
        for n in nums:
            if n in num_visited:
                res.append(n)
            else:
                num_visited.add(n)
        
        return res