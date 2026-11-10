class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max(sentence.count(' ') + 1 for sentence in sentences)