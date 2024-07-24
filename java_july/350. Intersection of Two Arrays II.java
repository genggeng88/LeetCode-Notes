class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        List<Integer> res = new ArrayList<>();

        int i=0, j=0, m=nums1.length, n=nums2.length;

        while (i<m && j<n) {
            if (nums1[i] < nums2[j]) {
                i++;
            }
            else if (nums1[i] > nums2[j]) {
                j++;
            }
            else {
                res.add(nums1[i]);
                i++;
                j++;
            }
        }
        int[] res2 = new int[res.size()];
        int idx = 0;
        for (int num : res) {
            res2[idx++] = num;
        }
        return res2;
    }
}