class Solution {
  public:

    string printString(string s, char ch, int count) {
        map<int, int> mp;
        bool found = false;
        int ans = 0;
        
        for(int i = 0; i < s.size(); i++){
            
            if(s[i] == ch){
                
                mp[s[i]]++;
            }
            if(mp[ch] == count){
                
                ans = i;
                found = true;
                break;
            }
        }
        if(found == false){
            
            return "";
        }
        return s.substr(ans+1);
        // Your code goes here
    }
};
