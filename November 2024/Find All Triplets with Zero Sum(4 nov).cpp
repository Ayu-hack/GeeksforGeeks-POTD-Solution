class Solution {
  public:
    vector<vector<int>> findTriplets(vector<int> &arr) {
        // CodeGenius
        vector<vector<int>>ans;
        for(int i=0;i<arr.size();i++){
            for(int j=i+1;j<arr.size();j++){
                for(int k=j+1;k<arr.size();k++){
                    if(arr[i]+arr[j]+arr[k]==0)ans.push_back({i,j,k});
                }
            }
        }
        return ans;
    }
};
