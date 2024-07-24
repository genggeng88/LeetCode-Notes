class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> map = new HashMap<>();
        List<Integer> res = new ArrayList<>();

        for (int num : nums1) {
            map.put(num, map.getOrDefault(num, 0)+1);
        }

        for (int num : nums2) {
            if (map.getOrDefault(num, 0) > 0) {
                res.add(num);
                map.put(num, map.get(num)-1);
            }
        }

        int[] inter = new int[res.size()];
        for (int i=0; i < res.size(); i++) {
            inter[i] = res.get(i);
        }
        return inter;
    }
}