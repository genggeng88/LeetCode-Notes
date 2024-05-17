class Solution {
    public int titleToNumber(String columnTitle) {
        Map<Character, Integer> mappings = new HashMap<>();
        char start = 'A';
        for(int i = 0; i<26; i++){
            mappings.put(start, i+1);
            start = (char)(start+1);
        }
        int n = columnTitle.length();
        int outcome = 0;
        for(int i=0; i<n; i++){
            outcome = outcome*26 + mappings.get(columnTitle.charAt(i));
        }
        return outcome;
    }
}