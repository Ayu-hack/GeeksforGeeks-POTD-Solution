class Solution {
  public:

    bool kPangram(string str, int k) {
        // code here
        map<char, int>mp;
        for(auto i:str) mp[i]++;
        int s = str.size() - mp[' '];
        mp.erase(' ');
        if(mp.size() == 26) return true;
        int rem = s - mp.size();
        int req = 26 - mp.size();
        return rem >= req and req <= k;
        
        
    }
};