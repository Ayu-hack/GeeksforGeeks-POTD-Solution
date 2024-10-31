class Solution:
    def maxStep(self, arr):
        ans = 0
        increase_count = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                increase_count += 1
            else:
                ans = max(ans, increase_count)
                increase_count = 0
        ans = max(ans, increase_count)
        return ans
