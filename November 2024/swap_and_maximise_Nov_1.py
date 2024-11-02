
class Solution:
    def maxSum(self,arr):
        arr.sort()
        new = []
        right=len(arr)-1
        left=0
        while left <= right:
            if left == right:
                new.append(arr[left])
                
                
            else :
                new.append(arr[left])
                new.append(arr[right])
            left+=1
            right-=1
        sum =0
        for i in range(0,len(new)-1):
            sum += abs(new[i] - new[i+1])
        sum += abs(new[-1]-new[0])
        return  sum
            
            


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  
        print(ans)  
        print("~")


if __name__ == "__main__":
    main()

