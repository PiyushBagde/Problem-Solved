class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        br = 0
        for i in range(len(word)):
            if word[i] == ch:
                br = i
                new_str = f"{word[br::-1]}{word[br+1:]}"
                return new_str
        return word
