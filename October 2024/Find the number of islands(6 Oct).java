// JAVA CODE

class Solution {
    public int numIslands(char[][] grid) {
        int n=grid.length, m=grid[0].length, ans=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]=='1')    ans++;
                dfs(i,j,n,m,grid);
            }
        }
        return ans;
    }
    int dir[][] = {{0,-1},{0,1},{1,0},{-1,0},{1,-1},{1,1},{-1,-1},{-1,1}};
    
    void dfs(int i,int j,int n,int m,char a[][]){
        if(i<0 || j<0 || i>=n || j>=m || a[i][j]=='0')  return;
        a[i][j]='0';
        for(int d[]:dir){
            dfs(d[0]+i, d[1]+j,n,m,a);
        }
    }

}
