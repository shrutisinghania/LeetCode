class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (n == 0)
            return;
        if (m == 0)
        {
            System.arraycopy(nums2, 0, nums1, 0, n);
            return;
        }
        int k = m;
        for (int i = m + n - 1; i >= n; i--)
            nums1[i] = nums1 [--k];
        k = 0;
        int j = n;
        for (int i = 0; i < m + n ; i++)
        {
            if( j < m+n && (k==n || nums1[j] <= nums2[k]))
                nums1[i] = nums1[j++];
            else
                nums1[i] = nums2[k++];
        }
    }
}