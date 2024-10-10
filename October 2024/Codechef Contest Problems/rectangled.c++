#include <bits/stdc++.h>
using namespace std;

int main()
{
  // your code goes here
  int T;
  cin >> T;
  while (T > 0)
  {
    T--;
    int n;
    int l = 0, b = 0;
    cin >> n;
    for (int i = 1; i < n; i++)
    {
      for (int j = 1; j < n; j++)
      {
        if ((i * j > l * b) && 2 * (i + j) <= n)
        {
          l = i;
          b = j;
        }
      }
    }
    cout << l * b << endl;
  }
}