class Solution {
  public:
    int minIncrements(vector<int> arr) {
        unordered_set<int> st;
        int n=arr.size();
        int sum=0,maxi=0;
        sort(arr.begin(),arr.end());
        for(int i=0;i<n;i++){
            maxi=max(maxi,arr[i]);
            if(st.find(arr[i])!=st.end()){
                maxi++;
                sum+=maxi-arr[i];
                st.insert(maxi);
            }else{
                st.insert(arr[i]);
            }
        }
        return sum;
    }
};
