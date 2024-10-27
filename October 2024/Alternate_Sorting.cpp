//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
#include <vector>
#include <algorithm>

class Solution {
  public:
    std::vector<int> alternateSort(std::vector<int>& arr) {
        std::sort(arr.begin(), arr.end());  // Sort in-place
        std::vector<int> result;
        int left = 0, right = arr.size() - 1;
        
        while (left <= right) {
            if (left != right) {
                result.push_back(arr[right--]);  // Largest remaining element
                result.push_back(arr[left++]);   // Smallest remaining element
            } else {
                result.push_back(arr[left++]);   // Middle element (for odd-sized arrays)
            }
        }
        
        return result;
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
        Solution obj;
        vector<int> ans = obj.alternateSort(arr);
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << " ";
        }
        cout << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends
