class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_sum = {}

        for i in jewels:
            stones_sum[i] = 0

        for i in stones:
            if i in stones_sum:
                stones_sum[i] += 1

        return sum(stones_sum.values())