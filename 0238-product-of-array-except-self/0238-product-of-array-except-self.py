class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post_num = 1
        pre_num = 1
        postfix = [1]
        prefix = [1]
        for i in range(len(nums)):
            pre_num *= nums[len(nums) - i - 1]
            prefix.append(pre_num)
            post_num *= nums[i]
            postfix.append(post_num)
        
        res = []

        for i in range(len(nums)):
            res.append(postfix[i]*prefix[len(nums) - i - 1])
        
        return res