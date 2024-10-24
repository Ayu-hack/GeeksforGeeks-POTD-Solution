
class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        k = len(arr)

        for i in range(0,k):
            if i == (k-1):
                break
            if (arr[i] != 0) & (arr[i+1] != 0) :
                if arr[i]==arr[i+1]:
                    arr[i]=2*arr[i]
                    arr[i+1]=0
                else:
                    continue
            else:
                continue
        zero = arr.count(0)
        for i in range(0,zero):
            arr.remove(0)
            arr.append(0)
        return arr
                
                
                

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1
