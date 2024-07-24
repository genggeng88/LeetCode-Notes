class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();

        ArrayList<Integer> tmp0 = new ArrayList<>();
        tmp0.add(1);
        res.add(tmp0);

        if (numRows == 1) {
            return res;
        }
        
        int row = 1;
        while (row < numRows) {
            ArrayList<Integer> tmp = new ArrayList<>();
            tmp.add(1);
            for (int i=1; i<row; i++){
                tmp.add(res.get(row-1).get(i-1) + res.get(row-1).get(i));
            }
            tmp.add(1);
            res.add(tmp);
            row++;
        }
        return res;
    }
}