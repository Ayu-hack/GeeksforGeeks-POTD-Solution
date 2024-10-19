#Given an array of integers arr[] of length N, every element appears thrice except for one which occurs once.
#Find that element which occurs once.
#jan 4th
class Solution:
    def singleElement(self, arr, N):
        # Initialize ones and twos
        ones = 0
        twos = 0

        # Iterate through the array
        for num in arr:
            # Update twos
            twos |= ones & num
            # Update ones
            ones ^= num
            # Calculate threes (common bits in ones and twos)
            threes = ones & twos
            # Remove common bits from ones and twos
            ones &= ~threes
            twos &= ~threes

        return ones


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.singleElement(arr,N))
# } Driver Code Ends
