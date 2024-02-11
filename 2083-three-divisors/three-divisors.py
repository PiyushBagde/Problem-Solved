class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        for div in range(1,n+1):
            if n % div == 0:
                count += 1

        if count == 3:
            return True
        else:
            return False

        