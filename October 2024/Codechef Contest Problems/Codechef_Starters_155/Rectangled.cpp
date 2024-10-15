#include <bits/stdc++.h>
#define int long long
#define float double
#define endl "\n"
using namespace std;


int32_t main()
{
    int t; cin >> t;
    while (t--)
    {
        int n; cin >> n;
        int peri = n/2;
        int l = 0, b = 0;
        while (l+b <= peri){
            if (l<b) l++;
            else b++;
        }
        cout << l*(--b) << endl;
   }
}