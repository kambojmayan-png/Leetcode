class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            target = num
            if num % 10 == num:
                return num
            num = 0
            while target / 10 != 0.0:
                num += target % 10
                target = target // 10

            