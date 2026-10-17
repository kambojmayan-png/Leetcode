class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int num = 0;
        for (int i = 0 ; i < nums.size() ; i++)
        {
            if (count == 0)
            {
                num = nums[i];
                count = 1;
            }
            else if (num == nums[i])
            {
                count++;
            }
            else 
            {
                count--;
            }
        }
        return num;
    }
};