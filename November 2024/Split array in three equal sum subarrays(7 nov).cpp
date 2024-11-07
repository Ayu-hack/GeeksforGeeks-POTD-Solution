class Solution {
  public:
    // Function to determine if array arr can be split into three equal sum sets.
    vector<int> findSplit(vector<int>& arr) {
        // code here
        int n = arr.size(), sum=0;
        for(int x:arr)sum+=x;
        if(sum%3)return {-1,-1};
        int requiredSum=sum/3;
        vector<int> ans;
        sum=0;
        for(int i=0;i<n;i++){
            sum+=arr[i];
            if(sum==requiredSum){
                ans.push_back(i);
                if(ans.size()==2)break;
                sum=0;
            }
        }
        if(ans.size()==2)return ans;
        return {-1,-1};
    }
};
