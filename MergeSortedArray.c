void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int i = m - 1;        // Pointer for the last element in nums1's valid part
    int j = n - 1;        // Pointer for the last element in nums2
    int k = m + n - 1;    // Pointer for the last position in nums1
    
    // Merge in reverse order
    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
    
    // If there are any remaining elements in nums2
    while (j >= 0) {
        nums1[k--] = nums2[j--];
    }

}