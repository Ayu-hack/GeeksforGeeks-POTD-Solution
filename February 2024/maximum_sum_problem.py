class Solution:
    def maxSum(self, n, memo={}): 
        if n == 0 or n == 1:
            return n
        if n in memo:
            return memo[n]
        memo[n] = max(n, self.maxSum(n // 2, memo) + self.maxSum(n // 3, memo) + self.maxSum(n // 4, memo))
        
        return memo[n]
