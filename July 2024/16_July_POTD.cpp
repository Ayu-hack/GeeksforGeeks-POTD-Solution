// User function template for C++
class Solution {
  public:

    string printString(string s, char ch, int count) {
       for(int i=0; i<s.size(); i++) {
           if(count == 0) return s.substr(i);
           else if(s[i] == ch) count--;
       }
       return "";
    }
};