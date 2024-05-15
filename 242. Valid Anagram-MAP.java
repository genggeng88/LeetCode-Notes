class Solution {
    public boolean isAnagram(String s, String t) {
        int ns = s.length();
        int nt = t.length();
        if(ns != nt){
            return false;
        }
        Map<Character, Integer> mapping = new HashMap<>();

        for(int i = 0; i < ns; i++){
            mapping.put(s.charAt(i), mapping.getOrDefault(s.charAt(i), 0)+1);
            mapping.put(t.charAt(i), mapping.getOrDefault(t.charAt(i), 0)-1);
        }

        for(char c : mapping.keySet()){
            if (mapping.get(c) != 0){
                return false;
            }
        }

        return true;
    }
}