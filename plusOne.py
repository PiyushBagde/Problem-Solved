def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = ''
        num = 0
        result = []
        for num in digits:
            res += str(num)
            num = int(res) + 1
            
        for test in str(num):
            result.append(int(test))

        return result  
    
