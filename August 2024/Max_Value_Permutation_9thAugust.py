class Solution:
    def Maximize(self, arr):
        # Get the length of array
        n = len(arr)
        
        # Sort the array
        arr.sort()
        
        # Initialize result
        result = 0
        MOD = 1000000007
        
        # Calculate sum of arr[i]*i
        for i in range(n):
            result = (result + (arr[i] * i)) % MOD
            
        return result

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.Maximize(A))
