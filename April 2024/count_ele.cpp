class Solution {
  public:
    vector<int> countElements(vector<int> &a, vector<int> &b, int n, vector<int> &query, int q) {
        // Sort the array b to use binary search
        std::sort(b.begin(), b.end());
        vector<int> result;

        // Process each query
        for (int i = 0; i < q; i++) {
            int x = query[i];  // Get the index from query array
            int target = a[x]; // Element from array a

            // Find the count of elements <= a[x] using binary search
            int count = upper_bound(b.begin(), b.end(), target) - b.begin();
            result.push_back(count);  // Store the result for the current query
        }

        return result;  // Return the result vector containing counts for each query
    }
};