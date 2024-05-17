class Solution {
    public int surfaceArea(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int total = 0;
        int sub = 0;

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] != 0){
                    total += 4*grid[i][j]+2;
                }
                if(i<m-1){
                    sub += Math.min(grid[i][j], grid[i+1][j]);
                }
                if(j<n-1){
                    sub += Math.min(grid[i][j], grid[i][j+1]);
                }
            }
        }

        return total - 2*sub;
    }
}