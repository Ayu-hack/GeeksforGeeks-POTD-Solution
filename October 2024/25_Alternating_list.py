class Solution:
    def alternateSort(self,arr):
        arr.sort()
        new = []
        right=len(arr)-1
        left=0
        while left <= right:
            if left == right:
                new.append(arr[left])
                
                
            else :
                
                new.append(arr[right])
                new.append(arr[left])
            left+=1
            right-=1
        return new

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

