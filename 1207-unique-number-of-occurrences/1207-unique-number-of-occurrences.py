class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hashmap = {}
        for i in arr:
            hashmap[i] = hashmap.get(i,0) + 1

        freq = hashmap.values()
        return len(set(freq)) == len(freq)           