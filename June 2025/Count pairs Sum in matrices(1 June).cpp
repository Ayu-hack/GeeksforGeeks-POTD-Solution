class Solution {
  public:
    int countPairs(vector<vector<int>> &mat1, vector<vector<int>> &mat2, int x) {
        // CodeGenius
        int n=mat1.size();
        int r1=0,c1=0,r2=n-1,c2=n-1; 
        int count=0;
        while(r1<n && r2>=0){
            int ele1=mat1[r1][c1];
            int ele2=mat2[r2][c2];
            if(ele1+ele2 == x){
                count++;
                c1++;
                c2--;
            }
            else if(ele1+ele2 < x) c1++;
            else c2--;
            
            if(c1==n){
                c1=0;
                r1++;
            }
            if(c2==-1){
                c2=n-1;
                r2--;
            }
        }
        return count;
        
    }
};
