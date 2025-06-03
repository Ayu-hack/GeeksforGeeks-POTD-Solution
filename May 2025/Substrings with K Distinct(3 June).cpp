class Solution {
  public:
    int atMost(string& s, int k){   
        int ans=0;
        int l=0, distinct=0;
        vector<int> freq(26,0);
        for(int r=0; r<s.length(); r++){
            if(freq[s[r]-'a']==0) distinct++;
            freq[s[r]-'a']++;
            while(distinct>k){
                freq[s[l]-'a']--;
                if(freq[s[l]-'a']==0) distinct--;
                l++;
            }
            ans+=r-l+1;
        }
        return ans;
    }
    int countSubstr(string& s, int k) {
        int ans=0;
        return atMost(s, k) - atMost(s, k-1);
    }
};
