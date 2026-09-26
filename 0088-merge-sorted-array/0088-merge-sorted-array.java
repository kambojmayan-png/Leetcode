class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] f = new int[n+m];
        int i = 0, j = 0;
        int a = 0;
        while(i<m && j <n)
        {
            if(nums1[i] <= nums2[j])
            {
                f[a] = nums1[i];
                a++;
                i++;
            }
            else
            {
                f[a] = nums2[j];
                a++;
                j++;
            }
        }
         while(i < m)
           {
                f[a] = nums1[i];
                a++;
                i++;
            }
            while(j < n)
            {
                f[a] = nums2[j];
                a++;
                j++;
            }
        for(int e = 0 ; e < m+n ; e++){
            nums1[e] = f[e];
        }
    }
}