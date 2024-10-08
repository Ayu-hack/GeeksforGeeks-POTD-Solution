// User function template for C++

// arr : given vector of elements
// target : given sum value

class Solution {
  public:
    int threeSumClosest(vector<int> ar, int target) {
        // Your code goes here
        sort(ar.begin(), ar.end());
        int n = ar.size(), ans = INT_MIN, dif = INT_MAX;
        for(int i=0; i<n; i++) {
            int l = i+1, r = n-1;
            while(l < r) {
                int sum = ar[i] + ar[l] + ar[r];
                if(sum == target) return target;
                else if(sum > target) r--;
                else l++;
                if(dif > abs(sum - target)) {
                    dif = abs(sum - target);
                    ans = sum;
                }
                else if(dif == abs(sum - target)) {
                    ans = max(ans, sum);
                }
            }
        }
        return ans;
    }
};