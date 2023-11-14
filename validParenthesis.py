def isValid(s): 
        """ 
        :type s: str 
        :rtype: bool 
        """ 
         
        stack = [] 
        sign = { 
            ")":"(", 
            "}":"{", 
            "]":"[" 
            } 
        if len(s) == 0: 
            return False 
        for item in  list(s): 
            if item in "({[": 
                stack.append(item) 
            else: 
                if len(stack) == 0: 
                    return False 
                if item in ")]}": 
                    if item == "]" and stack[-1] == sign[item]: 
                        stack.pop() 
                    elif item == "}" and stack[-1] == sign[item]: 
                        stack.pop() 
                    elif item == ")" and stack[-1] == sign[item]: 
                        stack.pop() 
                    else: 
                        return False 
                         
                     
        if len(stack) == 0: 
            return True 
     
                     
         
print(isValid(""))