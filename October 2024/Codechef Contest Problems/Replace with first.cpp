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
		int n = 0, x = 0, m = 0; cin >> n >> m;
		string a, b; cin >> a >> b;

		if (a == b) { cout << "0\n"; continue; }
		if (a[0] != b[0]) { cout << "-1\n"; continue; }

		if (n > m) {
			swap(a, b);
			swap(n, m);
		}

		int flag = 1;
		for (int i = 0; i < n; i++) {
			if (a[i] != b[i]) { flag = 0; break; }
		}
		if (flag) { cout << "1\n"; continue; }

		deque<char> A, B;
		for (int i = 0; i < n; i++) A.push_back(a[i]);
		for (int i = 0; i < m; i++) B.push_back(b[i]);

		while (!A.empty()) {
			if (A.front() == B.front()) {
				A.pop_front();
				B.pop_front();
			}
			else break;
		}
		while (!A.empty()) {
			if (A.back() == B.back()) {
				A.pop_back();
				B.pop_back();
			}
			else break;
		}

		if (A.empty()) cout << "1\n";
		else cout << "2\n";
	}
	return 0;
}