#User function Template for python3
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        seen = set()  # Set to keep track of elements within the window of size k
        for i in range(len(arr)):
            # If element is already in the set, we found a duplicate within distance k
            if arr[i] in seen:
                return True
            # Add the current element to the set
            seen.add(arr[i])
            # If the window size exceeds k, remove the oldest element (arr[i - k])
            if i >= k:
                seen.remove(arr[i - k])
        return False



#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends