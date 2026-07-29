class Solution(object):
    def isPalindrome(self, x):
        if(x < 0):
            return False
        num , reverse_num = x , 0
        while(num > 0):
            reverse_num = reverse_num*10 + num%10
            num = num//10
        return x == reverse_num 