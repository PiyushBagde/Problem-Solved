class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits) - 1

        digits[size] += 1

        for i in range(size, 0, -1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
            else:
                break

        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)

        return digits
            
