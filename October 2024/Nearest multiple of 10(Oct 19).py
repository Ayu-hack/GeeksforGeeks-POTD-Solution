#User function Template for python3
import sys
sys.set_int_max_str_digits(0)

class Solution:
    def roundToNearest (self, str1) : 
        #Complete the function
        l = len(str1)
        s = int(str1)
        if s%10 <= 5:
            s -= (s%10)
            s =  str(s).rjust(l,'0')
            return s
        else:
            s = (s - (s%10)) + 10
            s =  str(s).rjust(l,'0')
            return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)
    print("~")

# } Driver Code Ends