class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = {}
        for i in sentence:
            count[i] = count.get(i, 0) + 1

        return True if len(count) == 26 else False