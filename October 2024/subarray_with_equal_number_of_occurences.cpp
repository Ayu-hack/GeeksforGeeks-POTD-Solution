//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
// } Driver Code Ends

class Solution {
  public:
    int sameOccurrence(vector<int>& arr, int x, int y) {
        int count = 0;
        int prefix_sum = 0;
        unordered_map<int, int> freq_map; // to store frequency of prefix sums
        freq_map[0] = 1; // Initial condition for prefix sum of 0

        for (int num : arr) {
            if (num == x) {
                prefix_sum += 1; // Increment for x
            } else if (num == y) {
                prefix_sum -= 1; // Decrement for y
            }
            
            // If this prefix sum has been seen before, add its count to result
            count += freq_map[prefix_sum];
            
            // Increment the count of this prefix sum in the map
            freq_map[prefix_sum]++;
        }
        
        return count;
    }
};

//{ Driver Code Starts.
int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        string ks;
        getline(cin, ks);
        int x = stoi(ks);
        string ks1;
        getline(cin, ks1);
        int y = stoi(ks1);
        Solution ob;
        int ans = ob.sameOccurrence(arr, x, y);
        cout << ans << "\n";
    }
    return 0;
}
// } Driver Code Ends
