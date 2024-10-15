#include <bits/stdc++.h>
#define int long long
#define endl "\n"
using namespace std;


bool check(string s, string t){
    int i=0, j=0;
    while (s[i]==t[j] and j<t.size()) {
        i++;
        j++;
    }
    if (j==t.size()) return true;
    
    i += (s.size()-1-i) - (t.size()-1-j);
    while (s[i]==t[j] and j<t.size()) {
        i++;
        j++;
    }
    if (j==t.size()) return true;
    
    return false;
    
}


int32_t main()
{
    int t; cin >> t;
    while (t--){
        int n, m; cin >> n >> m;
        string s; cin >> s;
        string t; cin >> t;

        if (m>n){
            int temp = n;
            n = m;
            m = n;
            string temps = s;
            s = t;
            t = temps;
        }

        if (s==t) {
            cout<<0<<endl;
            continue;
        }
        else if (s[0] != t[0]) {
            cout<<-1<<endl;
            continue;
        }
        
        if (check(s, t)){
            cout<<1<<endl;
        }
        else{
            cout<<2<<endl;
        }
    }
}