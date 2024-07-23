class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        set1 = set()

        for word in words:
            code = ""
            for i in word:
                code += codes[ord(i) - 97]
            set1.add(code)

        return len(set1)
 
        
