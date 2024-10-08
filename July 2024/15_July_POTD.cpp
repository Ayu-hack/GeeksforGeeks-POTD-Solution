// User function Template for C++
class Solution {
  public:
    string smallestNumber(int s, int d) {
        if(d * 9 < s) return "-1";
        int ar[d] = {0};
        ar[0] = 1;
        s--;
        for(int i=d-1; i>=0 and s > 0; i--) {
            if(s > 9) {
                ar[i] = 9;
                s -= 9;
            }
            else {
                ar[i] += s;
                s = 0;
            }
        }
        string ans = "";
        for(auto i:ar) ans += to_string(i);
        return ans;
        
    }
};