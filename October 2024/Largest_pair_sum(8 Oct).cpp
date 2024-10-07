class Solution {
  public:
    int pairsum(vector<int> &arr) {
        
        sort(arr.begin(), arr.end());
        
        int n = arr.size();
        
        return arr[n-2] + arr[n-1];
        // code here
    }
};