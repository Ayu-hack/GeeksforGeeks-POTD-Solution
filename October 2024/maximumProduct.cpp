#include <iostream>
#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    long long maximumProduct(int n, vector<int> &arr, int l, int r) {
        long long maxInSubarray = LLONG_MIN;
        long long maxOutsideSubarray = LLONG_MIN;

        // Traverse through the array and find the maximum values in and outside the subarray
        for (int i = 1; i <= n; i++) {
            if (i >= l && i <= r) {
                maxInSubarray = max(maxInSubarray, (long long)arr[i - 1]);  // Max element inside the subarray
            } else {
                maxOutsideSubarray = max(maxOutsideSubarray, (long long)arr[i - 1]);  // Max element outside the subarray
            }
        }

        // If no element outside subarray is found (i.e., maxOutsideSubarray is still LLONG_MIN), return 0
        if (maxOutsideSubarray == LLONG_MIN) return 0;

        // Return the product of the maximum element from the subarray and outside the subarray
        return maxInSubarray * maxOutsideSubarray;
    }
};

int main() {
    // Input array size and elements
    int n;
    cout << "Enter the size of the array: ";
    cin >> n;

    vector<int> arr(n);
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Input l and r for subarray
    int l, r;
    cout << "Enter the values of l and r: ";
    cin >> l >> r;

    // Create a Solution object and call the function
    Solution sol;
    long long result = sol.maximumProduct(n, arr, l, r);

    // Output the result
    cout << "The maximum product is: " << result << endl;

    return 0;
}
