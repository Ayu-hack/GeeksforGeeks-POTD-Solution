// User function template for C++

class Solution {
  public:
    static bool cmp(const string &s1, const string &s2) {
        return s1.size() < s2.size();
    }
    string longestCommonPrefix(vector<string> arr) {
        // your code here
        if(arr.size() == 1) return arr[0];
        sort(arr.begin(), arr.end(), cmp);
        
        string s = arr[0], ans = "";
        for(int i=0; i<s.size(); i++) {
            string cur = s.substr(0, i);
            bool chk = true;
            for(int j=1; j<arr.size(); j++) {
                if(arr[j].substr(0, i) != cur) {
                    chk = false;
                    break;
                }
            }
            if(chk) ans = cur;
            else break;
        }
        if(ans == "") return "-1";
        return ans;
    }
};