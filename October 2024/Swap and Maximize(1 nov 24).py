class Solution:
    def maxSum(self, arr):
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Create a new array to arrange elements in the desired order
        n = len(arr)
        rearranged = []
        
        # Step 3: Use two pointers, one starting from the beginning and one from the end
        i, j = 0, n - 1
        while i <= j:
            if i == j:  # When there's only one element left
                rearranged.append(arr[i])
            else:
                rearranged.append(arr[i])
                rearranged.append(arr[j])
            i += 1
            j -= 1
        
        # Step 4: Calculate the maximum sum of absolute differences in the circular array
        max_sum = 0
        for k in range(n):
            max_sum += abs(rearranged[k] - rearranged[(k + 1) % n])
        
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends