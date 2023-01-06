class Solution {
    public void dfs(char[][] grid, int r, int c){
        int row = grid.length;
        int col = grid[0].length;
        if (r<0 || c<0 || r > row-1 || c>col-1 || grid[r][c]=='0'){
            return;
        }

        grid[r][c]='0';
        dfs(grid, r-1, c);
        dfs(grid, r+1, c);
        dfs(grid, r, c+1);
        dfs(grid, r, c-1);
    }

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }

        int nr = grid.length;
        int nc = grid[0].length;
        int num_islands = 0;

        for (int r = 0; r < nr; ++r) {
            for (int c = 0; c < nc; ++c) {
                if (grid[r][c] == '1') {
                    dfs(grid, r, c);
                    num_islands++;
                }
            }
        }
        return num_islands;
    }
}