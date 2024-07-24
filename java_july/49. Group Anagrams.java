class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        List<List<String>> res = new ArrayList<>();

        for (String s : strs) {
            char[] tmp = s.toCharArray();
            Arrays.sort(tmp);
            String key = new String(tmp);
            map.putIfAbsent(key, (new ArrayList<>()));
            map.get(key).add(s);
        }

        for (List<String> list : map.values()) {
            res.add(list);
        }

        return res;
    }
}