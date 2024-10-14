class Solution {
  public:
    int pairWithMaxSum(vector<int>& arr) {
        // CodeGenius
        int maxi=-1;
        for(int i=1;i<arr.size();i++){
            maxi=max(maxi,arr[i]+arr[i-1]);
        }
        return maxi;
    }
};
