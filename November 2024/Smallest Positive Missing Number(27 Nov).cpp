class Solution {
  public:
    int missingNumber(vector<int> &arr) {
        //CodeGenius
        int n=arr.size();
        for(int i=0;i<n;i++){
            while(arr[i]>=1 && arr[i]<=n && arr[i]!=arr[arr[i]-1]){
                swap(arr[i],arr[arr[i]-1]);
            }
        }
        for(int i=1;i<=n;i++){
            if(i!=arr[i-1]) return i;
        }
        return n+1;
    }
};
