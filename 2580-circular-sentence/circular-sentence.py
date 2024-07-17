class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lst = sentence.split()
        if lst[0][0] != lst[-1][-1]:
            return False
        
        for i in range(len(lst) - 1):
            if lst[i][-1] != lst[i+1][0]:
                return False
        
        return True
        