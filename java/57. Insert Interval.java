class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        LinkedList<int[]> res = new LinkedList<>();
        boolean inserted = false;
        
        for (int[] interval : intervals){
            if (!inserted) {
                if (newInterval[1] < interval[0]){
                    res.add(newInterval);
                    res.add(interval);
                    inserted = true;
                }
                else if(newInterval[0] > interval[1]){
                    res.add(interval);
                }
                else{
                    int left = Math.min(newInterval[0], interval[0]);
                    int right = Math.max(newInterval[1], interval[1]);
                    res.add(new int[]{left, right});
                    inserted = true;
                }
            }
            else {
                if (interval[0] > res.getLast()[1]){
                    res.add(interval);
                }
                else {
                    res.getLast()[0] = Math.min(res.getLast()[0], interval[0]);
                    res.getLast()[1] = Math.max(res.getLast()[1], interval[1]);
                }
            }
        }
        if (!inserted){
            res.add(newInterval);
        }
        return res.toArray(new int[res.size()][]);
    }
}