class Solution {
    private List<String> result;
    private Map<Character, String> mapping = Map.of(
        '2',"abc",'3',"def",'4',"ghi",'5',"jkl",
        '6',"mno",'7',"pqrs",'8',"tuv",'9',"wxyz"
    );

    public List<String> letterCombinations(String digits) {
        result = new ArrayList<>();
        int n = digits.length();
        if (n==0) {
            return result;
        }
        backtrack(digits, 0, new StringBuilder(), n);
        return result;
    }

    private void backtrack(String digits, int idx, StringBuilder path, int n) {
        if (idx == n) {
            result.add(path.toString());
            return;
        }
        String chars = mapping.get(digits.charAt(idx));
        for (char c : chars.toCharArray()) {
            path.append(c);
            backtrack(digits, idx+1, path, n);
            path.deleteCharAt(path.length()-1);
        }
    }
}