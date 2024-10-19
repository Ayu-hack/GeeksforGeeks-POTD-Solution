class Solution {
  public:
  void DFS(vector<vector<char>>& M, int r, int c) {
    int ROW = M.size();int COL = M[0].size();
    if (r < 0 || c < 0 || r >= ROW || c >= COL || M[r][c] != '1') {
        return;}
    M[r][c] = '0';
    vector<int> rNbr = {1, -1, 0, 0, 1, -1, 1, -1};
    vector<int> cNbr = {0, 0, 1, -1, 1, -1, -1, 1};
   for (int i = 0; i < 8; ++i) {

C++ (g++ 5.4)
Average Time: 20m



    int ROW = M.size();int COL = M[0].size();


 

Custom Input
        int newR = r + rNbr[i];
        int newC = c + cNbr[i];
        DFS(M, newR, newC);
    }}
    int numIslands(vector<vector<char>>& grid) {
        int ROW = grid.size();
    int COL = grid[0].size();
    int count = 0;
    for (int r = 0; r < ROW; r++) {
        for (int c = 0; c < COL; c++) {
            if (grid[r][c] == '1') {
                count++;
                DFS(grid, r, c);
            }}}
    return count;
    }
};
