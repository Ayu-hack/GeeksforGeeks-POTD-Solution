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
		int n = 0, x = 0, m = 0, flag = 0, FLAG = 2; cin >> n >> m;
		vector<vector<int>> arr(n, vector<int>(m, 2));

		// diagonal -> 3
		for (int i = 0, j = 0; i < n && j < m; i++, j++) arr[i][j] = 3;

		if (n > m) {
			for (int i = m; i < n; i++) arr[i][0] = 3;
		}
		else if (n < m) {
			for (int i = n; i < m; i++) arr[0][i] = 3;
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) cout << arr[i][j] << ' ';
			cout << endl;
		}

		cout << endl;
	}
	return 0;
}