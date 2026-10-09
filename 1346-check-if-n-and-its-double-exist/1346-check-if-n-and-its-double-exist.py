class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    continue

                if arr[i] == 2*arr[j]:
                    return True

        return False