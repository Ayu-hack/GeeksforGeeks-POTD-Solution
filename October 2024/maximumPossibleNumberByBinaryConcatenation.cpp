#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <bitset>

using namespace std;

class Solution {
public:
    int maxGoodNumber(vector<int>& nums) {
        int n = nums.size();
        vector<string> binaries;

        // Convert each number to a binary string and store in vector
        for (int num : nums) {
            binaries.push_back(toBinary(num));
        }

        // Sort binary strings to maximize concatenation
        sort(binaries.begin(), binaries.end(), [](const string &a, const string &b) {
            return a + b > b + a;
        });

        // Handle case where all numbers are zero
        if (binaries[0] == "0") return 0;

        // Concatenate all sorted binary strings
        string resultBinary = accumulate(binaries.begin(), binaries.end(), string());

        // Convert the final binary string to an integer and return it
        return stoll(resultBinary, nullptr, 2);
    }

    // Helper function to convert integer to a binary string (optimized)
    string toBinary(int num) {
        if (num == 0) return "0";
        return bitset<32>(num).to_string().substr(bitset<32>(num).to_string().find('1'));
    }
};

int main() {
    Solution sol;
    
    // Example test case
    vector<int> nums = {3, 30, 31};
    
    // Call the maxGoodNumber function and print the result
    int result = sol.maxGoodNumber(nums);
    cout << "Maximum possible number by binary concatenation: " << result << endl;

    return 0;
}

