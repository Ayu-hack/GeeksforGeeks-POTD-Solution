#include <bits/stdc++.h>
using namespace std;

bool isPrime(int n)
{
  // Since 0 and 1 is not prime
  // return false.
  if (n == 1 || n == 0)
    return false;

  // Run a loop from 2 to
  // square root of n.
  for (int i = 2; i * i <= n; i++)
  {
    // If the number is divisible by i,
    // then n is not a prime number.
    if (n % i == 0)
      return false;
  }

  // Otherwise n is a prime number.
  return true;
}

vector<int> firstnp(int n)
{
  int limit = max(15, static_cast<int>(n * log(n) + n * log(log(n))));
  vector<bool> isp(limit + 1, true);
  isp[0] = isp[1] = false;
  for (int p = 2; p * p <= limit; p++)
  {
    if (isp[p])
    {
      for (int m = p * p; m <= limit; m += p)
      {
        isp[m] = false;
      }
    }
  }

  vector<int> primes;
  for (int p = 2; primes.size() < n && p <= limit; p++)
  {
    if (isp[p])
      primes.push_back(p);
  }
  return primes;
}

int main()
{
  int t;
  cin >> t;
  while (t--)
  {
    int n, m;
    cin >> n >> m;
    int a[n][m];
    vector<int> v = firstnp(m * n);
    int count = 0;
    // sieve_of_eratosthenes(v);

    count = 0;
    for (int i = 0; i < n; i++)
    {
      for (int j = 0; j < m; j++)
      {
        a[i][j] = v[count];
        count++;
      }
    }

    for (int i = 0; i < n; i++)
    {
      for (int j = 0; j < m; j++)
      {
        cout << a[i][j] << " ";
      }
      cout << endl;
    }
  }
}