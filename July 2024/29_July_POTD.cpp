// User function template for C++
class Solution {
  public:
    int rowWithMax1s(vector<vector<int> > &arr) {
        // code here
        int ans = -1, temp = 0;
        for(int i=arr.size()-1; i>=0; i--) {
            int cur = 0;
            for(int j=arr[i].size()-1; j>=0; j--) {
                if(arr[i][j] == 1) cur++;
            }
            if(cur == 0) continue;
            if(cur >= temp) {
                temp = cur;
                // if(ans != -1) ans = min(ans, i);
                ans = i;
            }
        }
        return ans;
    