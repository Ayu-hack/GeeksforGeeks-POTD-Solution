#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    int findWinner(int n, int x, int y) {
        vector<bool> dp(n + 1, false);
        
        dp[0] = false; // If no moves left, the current player loses.
        dp[1] = true;  // If 1 stone, the current player wins.
        
        // Fill the dp array for each state up to n
        for (int i = 2; i <= n; i++) {
            // If removing 1 stone, x stones, or y stones leads to a losing state
            dp[i] = !dp[i - 1];  // If taking 1 stone leads to a losing state.
            
            if (i - x >= 0) {
                dp[i] = dp[i] || !dp[i - x];  // If taking x stones leads to a losing state.
            }
            if (i - y >= 0) {
                dp[i] = dp[i] || !dp[i - y];  // If taking y stones leads to a losing state.
            }
        }
        
        return dp[n];  // Return the result for n stones.
    }
};

int main() {
    int n, x, y;
    
    // Taking input for n, x, and y
    cout << "Enter the number of stones (n): ";
    cin >> n;
    cout << "Enter the value of x (stones to remove): ";
    cin >> x;
    cout << "Enter the value of y (stones to remove): ";
    cin >> y;
    
    // Create an instance of Solution class
    Solution sol;
    
    // Find the winner
    int result = sol.findWinner(n, x, y);
    
    // Output the result
    if (result == 1) {
        cout << "Player 1 wins!" << endl;
    } else {
        cout << "Player 2 wins!" << endl;
    }

    return 0;
}
