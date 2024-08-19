import java.util.*;
// import java.util.List;

class Solution {
    public long maximumValueSum(int[][] board) {
        int m = board.length, n = board[0].length;
        long maxSum = Long.MIN_VALUE;

        List<int[]> rowCombo = combo(m);
        List<int[]> colCombo = combo(n);

        for (int[] rows : rowCombo) {
            for (int[] cols : colCombo) {
                long currSum = 0;
                System.out.println("Testing Rows: " + rows[0] + ", " + rows[1] + ", " + rows[2]);
                System.out.println("Testing Cols: " + cols[0] + ", " + cols[1] + ", " + cols[2]);
                for (int i = 0; i < 3; i++) {
                    currSum += board[rows[i]][cols[i]];
                    System.out.println("Adding board[" + rows[i] + "][" + cols[i] + "] = " + board[rows[i]][cols[i]]);
                }
                System.out.println("Current Sum: " + currSum);
                maxSum = Math.max(maxSum, currSum);
            }
        }
        return maxSum;
    }

    private List<int[]> combo(int length) {
        List<int[]> tmp = new ArrayList<>();
        for (int i = 0; i < length - 2; i++) {
            for (int j = i + 1; j < length - 1; j++) {
                for (int k = j + 1; k < length; k++) {
                    tmp.add(new int[]{i, j, k});
                }
            }
        }
        return tmp;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] board = {
            {-3, 1, 1, 1},
            {-3, 1, -3, 1},
            {-3, 2, 1, 1}
        };
    
        System.out.println("Maximum Sum: " + sol.maximumValueSum(board)); // Expected output: 4
    }
}