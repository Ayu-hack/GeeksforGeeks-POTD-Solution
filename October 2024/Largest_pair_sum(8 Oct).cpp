class Solution {
  public:
    int pairsum(vector<int> &arr) {
        int mx1 = 0, mx2 = 0;
        for(int i=0; i<arr.size(); i++) {
            if(arr[i] > mx1) {
                mx2 = mx1;
                mx1 = arr[i];
            }
            else if(arr[i] > mx2) {
                mx2 = arr[i];
            }
        }
        return mx1 + mx2;
    }
};
