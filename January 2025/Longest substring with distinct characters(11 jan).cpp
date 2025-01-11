class Solution {
  public:
    int longestUniqueSubstr(string &s) {
        // CodeGenius
        vector<bool>vis(26,false);
        int maxi=INT_MIN;
        int l=0,r=0;
        while(r<s.size()){
            while(vis[s[r]-'a']==true){
                vis[s[l]-'a']=false;
                l++;
            }
            vis[s[r]-'a']=true;
            maxi=max(maxi,r-l+1);
            r++;
        }
        return maxi;
    }
};
