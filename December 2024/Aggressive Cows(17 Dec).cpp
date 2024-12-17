class Solution {
  public:

      bool isPossible(vector<int> &stalls,int k,int mid,int n){
        int c=1,prev=stalls[0];
        for(int i=1;i<n;i++){
            if(stalls[i]-prev>=mid){
                c++;
                prev=stalls[i];
            }
        }
        return c>=k;
    }
    int aggressiveCows(vector<int> &stalls, int k) {

        // Write your code here
        sort(stalls.begin(),stalls.end());
        int n=stalls.size(),low=0,high=stalls[n-1]-stalls[0],mid,ans=0;
        while(low<=high){
            mid=(low+high)/2;
            if(isPossible(stalls,k,mid,n)){
                ans=max(ans,mid);
                low=mid+1;
            }
            else high=mid-1;
        }
        return ans;
    }
};
