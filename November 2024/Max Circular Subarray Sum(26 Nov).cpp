class Solution {
  public:
    int circularSubarraySum(vector<int> &arr) {
        //CodeGenius
        int minSum=INT_MAX;
        int maxSum=INT_MIN;
        int s1=0,s2=0,TotalSum=0;
        for(int i=0;i<arr.size();i++){
            TotalSum+=arr[i];
            s1+=arr[i];
            s2+=arr[i];
            if(s1<0) s1=0;
            if(s2>0) s2=0;
            maxSum=max(maxSum,s1);
            minSum=min(minSum,s2);
        }
        return max(maxSum,TotalSum-minSum);
    }
};
