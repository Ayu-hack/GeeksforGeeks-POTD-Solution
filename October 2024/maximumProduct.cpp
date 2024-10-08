#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    long long maximumProduct(int n, vector<int> &arr, int l, int r) {
        // Initializing the first element from subarray and another from outside subarray
        long long num1 = LLONG_MIN;
        long long num2 = LLONG_MIN;

        // Find the maximum element from the subarray arr[l:r]
        for (int i = l; i <= r; i++) {
            num1 = max(num1, (long long)(arr[i - 1]));
        }

        // Find the maximum product of num1 with elements outside arr[l:r]
        for (int i = 1; i <= n; i++) {
            if (!(i >= l && i <= r)) {
                num2 = max(num2, num1 * arr[i - 1]);
            }
        }

        return num2;
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
