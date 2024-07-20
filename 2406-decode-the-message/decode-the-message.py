class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res = ""
        key = key.replace(" ","")
        new_key = ""

        for i in key:
            if i not in new_key:
                new_key += i
        
        for i in message:
            if i == " ":
                res += " "
            else:    
                idx = new_key.index(i)
                res += chr(97 + idx)
        return res

        