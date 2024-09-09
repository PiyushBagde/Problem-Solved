class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        j = 1
        max_length = 0
        unique = {fruits[i]:1}
        if len(fruits) == 1:
            return 1
        while j < len(fruits):
            if fruits[j] in unique:
                unique[fruits[j]] += 1
            else:
                unique[fruits[j]] = 1

            if len(unique) <= 2:
                max_length = max(max_length, j-i + 1)
            else:
                while len(unique) > 2:
                    unique[fruits[i]] -= 1
                    if unique[fruits[i]] == 0:
                        del unique[fruits[i]]
                    i += 1
                    
            j+=1
            
        return max_length
            