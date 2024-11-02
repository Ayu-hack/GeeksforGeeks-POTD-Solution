class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        seen = set()
    
        for i in range(len(arr)):
            if arr[i] in seen:
                return True
        
            seen.add(arr[i])
        
            if len(seen) > k:
                seen.remove(arr[i - k])
    
        return False


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
        print("~")
        t -= 1
