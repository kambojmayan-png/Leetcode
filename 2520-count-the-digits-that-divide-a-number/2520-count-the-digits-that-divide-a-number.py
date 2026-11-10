class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        nums = num

        while nums != 0:

            if num % (nums % 10) == 0:
                count += 1 
                
            nums = nums // 10
        
        return count