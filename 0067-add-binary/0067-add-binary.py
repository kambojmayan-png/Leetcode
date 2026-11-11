class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aNum = 0
        bNum = 0
        for i in range(len(a) - 1, -1, -1):
            aNum += (2 ** i)*int(a[len(a) - 1 - i])

        for i in range(len(b) - 1, -1, -1):
            bNum += (2 ** i)*int(b[len(b) - 1 - i])
        
        resNum = aNum + bNum

        if resNum == 0:
            return "0"

        res = ""

        while resNum != 0:

            res += str(resNum % 2)
            resNum = resNum//2

        return res[::-1]