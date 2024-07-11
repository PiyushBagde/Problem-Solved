class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        size = len(command)
        i = 0
        while i < size:
            if command[i] == '(':
                if command[i+1] == ')':
                    i = i+2
                    result += 'o'
                else:
                    result += command[i+1:i+3]
                    i = i + 4
            else:
                result += command[i]
                i+=1
        return result 
                
        



        