#include "bits/stdc++.h"
using namespace std;

#define int long long
#define mod 1000000007
#define endl '\n'

signed main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int test = 0; cin >> test;
	while (test--)
	{
		int n = 0, x = 0, k = 0, maxm = 2e6, sum = maxm; cin >> n;
		vector<int> b(n), a(n);

		for (int i = 0; i < n; i++) cin >> b[i];
		cout << maxm << ' ';

		for (int i = 1; i < n; i++) {
			x = b[i] - sum + maxm;
			cout << x << ' ';
			sum += x;
		}
		cout << endl;
	}
	return 0;
}