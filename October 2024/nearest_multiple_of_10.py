import sys
class Solution:
    def roundToNearest (self, str2) :
        sys.set_int_max_str_digits(50000)
        i=0
        count=0
        r=len(str2)
        for i in range(0,r):
            if str2[i] == '0':
                count += 1
            else:
                break
        k = int(str2)
        rem = k%10
        if rem >5:
            r=10-rem
            p=k+r
            if count==0:
                return p
            else:
                str1 = str(p)
                for i in range(0,count):
                    str1 = "0" + str1
                return str1
            
        elif rem<=5:
            
            q=k-rem
            if count==0:
                return q
            else:
                str1 = str(q)
                for i in range(0,count):
                    str1 = "0" + str1
                return str1
            
        
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

