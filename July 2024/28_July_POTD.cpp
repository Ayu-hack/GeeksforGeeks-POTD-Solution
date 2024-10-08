// User function template for C++
class Solution {
  public:

    string removeDups(string str) {
        // Your code goes here
        set<char>st;
        string ans = "";
        for(auto i:str) {
            if(st.find(i) != st.end()) continue;
            ans += i;
            st.insert(i);
        }
        return ans;
    }
};