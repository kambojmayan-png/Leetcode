class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        if len(sentences) == 0:
            return 0
        count = 0
        res = 0
        for i in sentences:
            count = 1
            for j in i:
                if j == " ":
                    count += 1
            res = max(count, res)
            
        return res