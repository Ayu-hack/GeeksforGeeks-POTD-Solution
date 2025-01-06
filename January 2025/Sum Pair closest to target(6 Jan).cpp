class Solution {
  public:
    vector<int> sumClosest(vector<int>& arr, int target) {
        // code here
        sort(arr.begin(),arr.end());
        int i=0,j=arr.size()-1,diff=INT_MAX,first=-1,second=-1;
        while(i<j){
            int sum=arr[i]+arr[j];
            if((diff>abs(sum-target)) || ((diff==abs(sum-target)) && arr[j]-arr[i]>second-first)){
                first=arr[i];
                second=arr[j];
                diff=abs(sum-target);
            }
            if(sum<=target)i++;
            else j--;
        }
        if(first==-1 and second==-1)return {};
        return {first,second};
    }

};
