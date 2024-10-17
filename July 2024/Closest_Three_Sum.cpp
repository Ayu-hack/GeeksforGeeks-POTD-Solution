class Solution {
public:
    int threeSumClosest(vector<int>& arr, int target) {
        sort(arr.begin(), arr.end());
        int closest_sum = INT_MAX;
        int n = arr.size();

        for (int i = 0; i < n - 2; ++i) {
            int left = i + 1, right = n - 1;

            while (left < right) {
                int current_sum = arr[i] + arr[left] + arr[right];

                if (current_sum == target) {
                    return current_sum;
                }

                if (abs(current_sum - target) < abs(closest_sum - target) || 
                   (abs(current_sum - target) == abs(closest_sum - target) && current_sum > closest_sum)) {
                    closest_sum = current_sum;
                }

                if (current_sum < target) {
                    ++left;
                } else {
                    --right;
                }
            }
        }
        return closest_sum;
    }
};
