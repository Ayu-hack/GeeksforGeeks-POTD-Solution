class Solution {
public:
    int rectanglesInCircle(int R) {
        int ans = 0;
        int limit = 2 * R * 2 * R; 
        for (int i = 1; i < 2 * R + 1; i++) {
            for (int j = 1; j < 2 * R + 1; j++) {
                if (i * i + j * j <= limit) {
                    ans++;
                }
            }
        }
        return ans;
    }
};
