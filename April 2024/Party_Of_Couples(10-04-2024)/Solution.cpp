#include <iostream>
using namespace std;

class Solution {
public:
    int findSingle(int n, int arr[]) {
        // Initialize answer with the first element of the array
        int ans = arr[0];
        
        // XOR every element with ans to find the single person
        for (int i = 1; i < n; i++) {
            ans = ans ^ arr[i];
        }
        
        // Return the single person
        return ans;
    }
};

int main() {
    int n;  // Number of people in the party (size of the array)
    cout << "Enter the number of people in the party: ";
    cin >> n;

    int arr[n];  // Array to store people's identifiers
    cout << "Enter the people (as integer values): ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Solution solution;
    int singlePerson = solution.findSingle(n, arr);
    
    cout << "The only single person is: " << singlePerson << endl;
    
    return 0;
}


/*
Explanation:
Input:

n: Number of people in the party (size of the array).
arr[]: An array where each number represents a person. Couples have the same integer value.
Logic:

We initialize ans with the first element of the array.
We then XOR each subsequent element with ans. Due to the properties of XOR (where a ^ a = 0 and a ^ 0 = a), paired elements cancel each other out, and the single person remains.
Finally, ans will contain the only unpaired element, which is returned as the single person.
Example:

Input:
makefile
Copy code
n = 5
arr = {1, 2, 3, 2, 1}
Output:

Copy code
The only single person is: 3

*/