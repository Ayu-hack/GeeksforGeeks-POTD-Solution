//15th July POTD
string LargestSwap(string S) {
        int n = S.length();
        
        // Store the last occurrence of each digit in the string
        vector<int> last(10, -1);
        for (int i = 0; i < n; i++) {
            last[S[i] - '0'] = i;
        }
        
        // Traverse through the string to find the best swap
        for (int i = 0; i < n; i++) {
            for (int d = 9; d > S[i] - '0'; d--) {
                // Check if there exists a digit larger than S[i] and it occurs later
                if (last[d] > i) {
                    // Swap the two digits
                    swap(S[i], S[last[d]]);
                    return S;
                }
            }
        }
        
        // If no swap can make it larger, return the original string
        return S;
    }
