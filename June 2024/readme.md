class Solution {
public:
    int findSwapValues(int a[], int n, int b[], int m) {
        int sumA = accumulate(a, a + n, 0);
        int sumB = accumulate(b, b + m, 0);
        
        if ((sumA - sumB) % 2 != 0) {
            return -1;
        }
        
        int target = (sumA - sumB) / 2;
        unordered_set<int> setB(b, b + m);
        
        for (int i = 0; i < n; ++i) {
            if (setB.find(a[i] - target) != setB.end()) {
                return 1;
            }
        }
        
        return -1;
    }
};
