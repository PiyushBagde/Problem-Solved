class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxlen = 0

        for sent in sentences:
            lst = list(map(str, sent.split(" ")))

            if len(lst) > maxlen:
                maxlen = len(lst)
        return maxlen


        