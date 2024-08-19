class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        backtrack(result, sb, 0, 0, n);

        return result;
    }

    private void backtrack(
        List<String> result, 
        StringBuilder curString,
        int left, 
        int right,
        int n
    ) {
        if (curString.length() == 2*n) {
            result.add(curString.toString());
            return;
        }
        if (left < n) {
            curString.append('(');
            backtrack(result, curString, left+1, right, n);
            curString.deleteCharAt(curString.length() - 1);
        }
        if (left > right) {
            curString.append(')');
            backtrack(result, curString, left, right+1, n);
            curString.deleteCharAt(curString.length() - 1);
        }
    }
}