class Solution {
    public void solve(char[][] board) {
        int nr = board.length;
        int nc = board[0].length;
        List<Integer> boarder = new LinkedList<>();

        for(int r=0; r<nr; r++){
            boarder.add(r*nc);
            boarder.add(r*nc + nc-1);
        }

        for(int c=1; c<nc-1; c++){
            boarder.add(c);
            boarder.add((nr-1)*nc + c);
        }

        for(int idx: boarder){
            int new_r = idx/nc;
            int new_c = idx%nc;
            DFS(board, new_r, new_c);
        }

        for(int r=0; r<nr; r++){
            for(int c=0; c< nc; c++){
                if(board[r][c]=='O'){
                    board[r][c]='X';
                }
                if(board[r][c]=='E'){
                    board[r][c]='O';
                }
            }
        }
    }

    public void DFS(char[][] board, int r, int c){
        int nr = board.length;
        int nc = board[0].length;
        if(board[r][c] != 'O'){
            return;
        }
        board[r][c] = 'E';
        if(c+1<nc){
            DFS(board, r, c+1);
        }
        if(c-1>=0){
            DFS(board, r, c-1);
        }
        if(r+1<nr){
            DFS(board, r+1, c);
        }
        if(r-1>=0){
            DFS(board, r-1, c);
        }        
    }
}