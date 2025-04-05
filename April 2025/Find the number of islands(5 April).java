class Solution {

    // A function to check if a given
    // cell (r, c) can be included in dfs
    public boolean isSafe(char[][] grid, int r, int c) {
        int row = grid.length;
        int col = grid[0].length;

        // r is in range, c is in range, value
        // is L and not yet visited
        return (r >= 0) && (r < row) && (c >= 0) && (c < col) && grid[r][c] == 'L';
    }

    public void dfs(char[][] grid, int r, int c) {

        // These arrays are used to get
        // r and c numbers of 8
        // neighbours of a given cell
        int[] rNbr = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] cNbr = {-1, 0, 1, -1, 1, -1, 0, 1};

        // Mark this cell as visited
        grid[r][c] = 'W';

        // Recur for all connected neighbours
        for (int k = 0; k < 8; ++k) {
            int newR = r + rNbr[k];
            int newC = c + cNbr[k];
            if (isSafe(grid, newR, newC)) {
                dfs(grid, newR, newC);
            }
        }
    }

    // Function to find the number of islands.
    public int countIslands(char[][] grid) {
        int row = grid.length;
        int col = grid[0].length;

        // Initialize count as 0 and traverse through
        // all cells of the given matrix
        int count = 0;
        for (int r = 0; r < row; ++r) {
            for (int c = 0; c < col; ++c) {

                // If a cell with value L is found,
                // then a new island is found
                if (grid[r][c] == 'L') {

                    // Visit all cells in this island.
                    dfs(grid, r, c);

                    // increment the island count
                    ++count;
                }
            }
        }
        return count;
    }
}
