class Solution {
  public:
    // Function to count the number of possible triangles.
     int countTriangles(vector<int>& arr) {
        // code here
        sort(arr.begin(),arr.end());
        int n=arr.size(),ans=0;
        for(int i=n-1;i>=2;i--){
            int j=0,k=i-1;
            while(j<k){
                int twoSideSum = arr[j]+arr[k];
                if(twoSideSum>arr[i]){
                    ans+=k-j;
                    k--;
                }
                else j++;
            }
        }
        return ans;
    }


};
