import java.util.*;

class Solution {
    ArrayList<String> res = new ArrayList<>();

    private void func(int row, int col, StringBuilder path, int[][] visited, int[][] maze, int n) {
        // Base case: reached destination
        if (row == n - 1 && col == n - 1) {
            res.add(path.toString());
            return;
        }

        // Direction vectors: D, L, R, U
        int[] dRow = {1, 0, 0, -1};
        int[] dCol = {0, -1, 1, 0};
        char[] dir = {'D', 'L', 'R', 'U'};

        for (int i = 0; i < 4; i++) {
            int nextRow = row + dRow[i];
            int nextCol = col + dCol[i];

            if (nextRow >= 0 && nextRow < n && nextCol >= 0 && nextCol < n &&
                visited[nextRow][nextCol] == 0 && maze[nextRow][nextCol] == 1) {
                
                visited[nextRow][nextCol] = 1;
                path.append(dir[i]);

                func(nextRow, nextCol, path, visited, maze, n);

                // Backtrack
                path.deleteCharAt(path.length() - 1);
                visited[nextRow][nextCol] = 0;
            }
        }
    }

    public ArrayList<String> ratInMaze(int[][] maze) {
        ArrayList<String> res = new ArrayList<>();
        int n = maze.length;

        if (maze[0][0] == 0 || maze[n - 1][n - 1] == 0) return res;

        int[][] visited = new int[n][n];
        visited[0][0] = 1;

        func(0, 0, new StringBuilder(), visited, maze, n);
        return this.res;
    }
}

// | Index | Direction | `dRow[i]` | `dCol[i]` | Moves to     |
// | ----- | --------- | --------- | --------- | ------------ |
// | 0     | Down      | +1        | 0         | (row+1, col) |
// | 1     | Left      | 0         | -1        | (row, col-1) |
// | 2     | Right     | 0         | +1        | (row, col+1) |
// | 3     | Up        | -1        | 0         | (row-1, col) |
