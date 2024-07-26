class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total = 0
        for i in range(1, ceil(math.sqrt(num))):
            if num % i == 0:
                total += i
            if num % (num/i) == 0 and num != num/i:
                total += num/i

            if total > num:
                return False

        return total == num 

