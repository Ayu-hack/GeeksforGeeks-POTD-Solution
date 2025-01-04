class Solution {
  public:
    int countTriplets(vector<int> &arr, int target) {
        // CodeGenius
        int count=0;
        int n=arr.size();
        for(int i=0;i<=n-3;i++){
            int j=i+1,k=n-1;
            while(j<k){
                int sum=arr[i]+arr[j]+arr[k];
                if(sum>target) k--;
                else if(sum<target)j++;
                else if(sum==target){
                    count++;
                    int temp=j+1;
                    while(temp<k&& arr[temp]==arr[temp-1])count++,temp++;
                    k--;
                }
            }
        }
        return count;
    }
};
