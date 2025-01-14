class Solution {
  public:
    // Function to find equilibrium point in the array.
    int findEquilibrium(vector<int> &arr) {
        // code here
        int n=arr.size(),right=0,left=0;
        for(int x:arr)right+=x;
        for(int i=0;i<n;i++){
            right-=arr[i];
            if(left==right)return i;
            left+=arr[i];
        }
        return -1;
    }

};
