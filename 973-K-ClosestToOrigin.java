class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int n = points.length;
        int[][] results = new int[k][2];
        int[] dst = new int[n];

        for(int i=0; i<n; i++){
            dst[i] = distance(points[i]);
        }
        Arrays.sort(dst);

        int thres = dst[k-1];
        int p=0;

        for(int j=0; j<n; j++){
            if (distance(points[j]) <= thres){
                results[p++] = points[j];
            }
        }
        return results;
    }
    public int distance(int[] point){
        return point[0]*point[0] + point[1]*point[1];
    }
}