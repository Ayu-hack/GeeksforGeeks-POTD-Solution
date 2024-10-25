class Solution:
    def editDistance(self, str1, str2):
        m = len(str1)
        n = len(str2)
        
        # Create a DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize the first column and first row
        for i in range(m + 1):
            dp[i][0] = i  # Deleting all characters from str1
        for j in range(n + 1):
            dp[0][j] = j  # Inserting all characters to form str2
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # No operation needed
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,    # Deletion
                        dp[i][j - 1] + 1,    # Insertion
                        dp[i - 1][j - 1] + 1  # Replacement
                    )
        
        return dp[m][n]

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)
