class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        if len(arr) < 2:
            return -1
        maximum = 0
        for i in range(len(arr)-1):
            small = arr[i] + arr[i+1]
            maximum = max(small,maximum)
        return maximum


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    t = int(data[0])
    lines = data[1:]

    for line in lines:
        s = list(map(int, line.strip().split()))
        solution = Solution()
        res = solution.pairWithMaxSum(s)
        print(res)

# } Driver Code Ends