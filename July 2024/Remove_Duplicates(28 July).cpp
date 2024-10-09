class Solution {
  public:

    string removeDups(string s) {
        
        map<char, int> mp;
        string res = "";
        
        for(int i = 0; i < s.size(); i++){
            
            if(mp.find(s[i]) == mp.end()){
                
                res += s[i];
                mp[s[i]]++;
            }
        }
        return res;
        // Your code goes here
    }
};