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
        vector<string> binaries;  // Store binary representations as strings

        // Convert each number to binary string and store it in the vector
        for (int i = 0; i < n; i++) {
            binaries.push_back(getBinary(nums[i]));
        }

        // Sort the binary strings to maximize the concatenated result
        sort(binaries.begin(), binaries.end(), compareBinary);

        // If the largest binary string is "0", return 0 (handles all-zero cases)
        if (binaries[0] == "0") return 0;

        // Concatenate the sorted binary strings
        string res = "";
        for (const string& bin : binaries) {
            res += bin;
        }

        // Convert the final concatenated binary string to integer and return it
        return binaryToInt(res);
    }

    // Custom comparator to get the largest concatenation
    static bool compareBinary(const string &a, const string &b) {
        return a + b > b + a;
    }

    // Convert binary string to integer, handle large numbers with stoll
    long long binaryToInt(const string& bin) {
        return stoll(bin, nullptr, 2);  // Use stoll for large binary strings
    }

    // Convert an integer to a binary string
    string getBinary(int q) {
        if (q == 0) return "0";
        return bitset<32>(q).to_string().substr(bitset<32>(q).to_string().find('1'));
    }
};

// Main function to test the solution
int main() {
    Solution sol;
    
    // Example test case
    vector<int> nums = {3, 30, 31};
    
    // Call the maxGoodNumber function and print the result
    int result = sol.maxGoodNumber(nums);
    cout << "Maximum possible number by binary concatenation: " << result << endl;

    return 0;
}
