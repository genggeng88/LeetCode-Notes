class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        int len1 = nums1.length, len2 = nums2.length;
        List<List<Integer>> answer = new LinkedList<>();
        Set<Integer> store = new HashSet<>();
        Set<Integer> res = new HashSet<>();
        Set<Integer> added = new HashSet<>();

        for(int i=0; i<len1; i++){
            store.add(nums1[i]);
        }
        for(int i=0; i<len2; i++){
            if(store.contains(nums2[i])){
                res.add(nums2[i]);
            }
        }
        List<Integer> uni1 = new LinkedList<>();
        List<Integer> uni2 = new LinkedList<>();
        for(int i=0; i<len1; i++){
            if(!res.contains(nums1[i]) && !added.contains(nums1[i])){
                uni1.add(nums1[i]);
                added.add(nums1[i]);
            }
        }
        added = new HashSet<>();
        for(int i=0; i<len2; i++){
            if(!res.contains(nums2[i]) && !added.contains(nums2[i])){
                uni2.add(nums2[i]);
                added.add(nums2[i]);
            }
        }
        answer.add(uni1);
        answer.add(uni2);
        return answer;
    }
}