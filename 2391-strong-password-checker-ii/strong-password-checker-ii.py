class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        l = u = d = sp = False
        chars = "!@#$%^&*()-+"

        for i in range(len(password) - 1):
            if password[i] == password[i+1]:
                return False
            
        for i in password:
            if i.islower():
                l = True
            if i.isupper():
                u = True
            if i.isdigit():
                d = True
            if i in chars:
                sp = True
            
        return l==u==d==sp

        
        