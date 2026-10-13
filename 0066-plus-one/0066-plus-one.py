class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1 , -1 , -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        newDigits = [0]*(len(digits) + 1)
        newDigits[0] = 1
        return newDigits