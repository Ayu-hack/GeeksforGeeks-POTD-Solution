class Solution:
    def maxOccured(self, n, l, r, maxx):
        a = [0] * (maxx + 2)
        for i in range(n):
            a[l[i]] += 1
            if r[i] + 1 <= maxx:
                a[r[i] + 1] -= 1
        
        maxCount = a[0]
        result = 0
        for i in range(1, maxx + 1):
            a[i] += a[i - 1]
            if a[i] > maxCount:
                maxCount = a[i]
                result = i
        
        return result
