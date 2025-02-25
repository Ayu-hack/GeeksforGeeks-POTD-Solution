class Solution {
  public:
    int getMaxArea(vector<int> &arr) {
        int n = arr.size();
        vector<int>prev(n,-1);
        vector<int>nex(n,n);
        stack<int>st;
        for(int i=0;i<n;i++){
            while(!st.empty() and arr[st.top()] >= arr[i]){
                st.pop();
            }
            if(!st.empty()){
                prev[i] = st.top();
            }
            st.push(i);
        }
        while(!st.empty()){
            st.pop();
        }
        for(int i=n-1;i>=0;i--){
            while(!st.empty() and arr[st.top()] >= arr[i]){
                st.pop();
            }
            if(!st.empty()){
                nex[i] = st.top();
            }
            st.push(i);
        }
        int ans = 0;
        for(int i=0;i<n;i++){
            ans = max(ans,arr[i]*(nex[i]-prev[i]-1));
        }
        return ans;
    }
};
