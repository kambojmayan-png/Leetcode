class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     
        freqMap = Counter(nums)
       
        arr = list(freqMap.items())
       
        for i in range(len(arr)):
            index = i
            for j in range(i + 1, len(arr)):
                if arr[j][1] > arr[index][1]:   
                    index = j
            arr[i], arr[index] = arr[index], arr[i]  
  
        final = []
        for i in range(k):
            final.append(arr[i][0])  

        return final
