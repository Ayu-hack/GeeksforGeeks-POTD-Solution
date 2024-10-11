//{ Driver Code Starts
#include <bits/stdc++.h>
#include <iostream>
using namespace std;
class Solution {
  public:
    vector<int> rearrange(vector<int>& arr) {
        // Code here
        int n = arr.size();
        unordered_set<int> s;
          for(int i=0; i<n; i++)
          {
            if(arr[i] != -1)
              s.insert(arr[i]);
          }
          for(int i=0; i<n; i++)
          {
            if(s.find(i) != s.end())
            {
              arr[i] = i;
            }
            else
            {
              arr[i] = -1;
            }
          }
          
          return arr;
    }
};
int main() {
    int t;
    cin >> t;
    cin.ignore();

    while (t--) {
        string input;
        getline(cin, input);
        stringstream ss(input);
        vector<int> arr;
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution solution;
        vector<int> ans = solution.rearrange(arr);

        for (int i = 0; i < ans.size(); i++)
            cout << ans[i] << " ";
        cout << endl;
    }

    return 0;
}
