class Solution {
public:
    vector<int> sortArray(vector<int>& arr, int A, int B, int C) {
        vector<int> result;

        // Traverse each element in the input array
        for (int& x : arr) {
            // Apply the quadratic equation: A*x^2 + B*x + C
            int ans = A * x * x + B * x + C;
            result.push_back(ans); // Store the result in the new array
        }

        // Sort the transformed array
        sort(result.begin(), result.end());

        return result; // Return the sorted transformed array
    }
};
