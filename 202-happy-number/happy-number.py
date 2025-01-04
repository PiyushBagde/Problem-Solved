class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        num_visited = set()
      
        def next_number(n):
            num = 0
            while n != 0:
                rem = n % 10
                num = num + rem ** 2
                n = n / 10
            return num

        while n not in num_visited:
            num_visited.add(n)
            n = next_number(n)
            if n == 1:
                return True
            
        return False
        
        