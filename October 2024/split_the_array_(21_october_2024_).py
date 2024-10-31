class Solution:
    def countgroup(self, arr):
        mod = int(1e9 + 7)
        xr = 0
        n = len(arr)
        for num in arr:
            xr ^= num
        if xr != 0:
            return 0
        ans = 1
        for _ in range(n - 1):
            ans = (ans * 2) % mod
        return ans - 1
