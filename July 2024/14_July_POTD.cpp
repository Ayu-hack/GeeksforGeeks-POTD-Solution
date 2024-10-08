// User function template for C++

class Solution {
  public:
    void segregate0and1(vector<int> &arr) {
        // code here
        int ind = 0;
        for(int i=0; i<arr.size(); i++) {
            if(arr[i] == 0) {
                arr[ind] = 0;
                ind++;
            }
        }
        for(int i=ind; i<arr.size(); i++) arr[i] = 1;
    }
};