class Solution {
  public:
    vector<int> countDistinct(vector<int> &arr, int k) {
        // code here.
        int n=arr.size(),j=0;
        vector<int> ans;
        unordered_map<int,int> frequency;
        for(int i=0;i<n;i++){
            frequency[arr[i]]++;
            if(i>=k-1){
                ans.push_back(frequency.size());
                frequency[arr[j]]--;
                if(frequency[arr[j]]==0)frequency.erase(arr[j]);
                j++;
            }
        }
        return ans;
    }
};
