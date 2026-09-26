class Solution:
    def isHappy(self, n: int) -> bool:

        hashmap = {}

        while True:
            a = []
            no = 0

            while n != 0:
                a.append(n % 10)
                n //= 10

            for i in a:
                no += i * i

            if hashmap.get(no, 0) != 0:
                return False

            hashmap[no] = 1

            if no == 1:
                return True

            n = no