import math as m

class Solution:
    def totalCount(self, k, arr):
        # code here
        ans = 0
        for i in range(len(arr)):
            ans += m.ceil(arr[i] / k)
        return ans