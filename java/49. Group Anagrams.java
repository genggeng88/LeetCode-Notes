class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        if(strs.length < 2){
            List<String> ele = new ArrayList<>();
            ele.add(strs[0]);
            res.add(ele);
            return res;
        }
        List<String> el = new ArrayList<>();
        el.add(strs[0]);
        res.add(el);
        int n = strs.length;
        for(int i=1; i<n; i++){
            boolean flag = false;
            for(int j=0; j<res.size(); j++){
                if(isAnagram(strs[i], res.get(j).get(0))){
                    flag = true;
                    res.get(j).add(strs[i]);
                }
            }
            if(!flag){
                List<String> el2 = new ArrayList<>();
                el2.add(strs[i]);
                res.add(el2);
            }
        }
        return res;
    }

    public boolean isAnagram(String s, String t) {
        int ns = s.length();
        int nt = t.length();
        if(ns != nt){
            return false;
        }
        char[] cs = s.toCharArray();
        char[] ct = t.toCharArray();
        Arrays.sort(cs);
        Arrays.sort(ct);

        return Arrays.equals(cs, ct);
    }
}