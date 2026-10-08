class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashmap = {}
        for i in s:
            if i in hashmap:
                return i
            hashmap[i] = 1