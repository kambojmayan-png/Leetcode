class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        number = 0
        n = len(num)
        for i in range(n - 1, -1, -1):
            power = n - 1 - i
            number += num[i] * (10 ** power)

        number += k
        
        if number == 0:
            return [0]

        res = []
        while number != 0:
            res.append(number % 10)
            number = number // 10

        return res[::-1]