class Solution {
  public:
    int sumSubstrings(string &s) {
        long long res=0,f=0;
        for(int i=0;i<s.size();++i){
            f=f*10+(s[i]-'0')*(i+1);
            res+=f;
        }
        return (int)res;
    }
};
