class Solution:
    def findTriplet(self, arr):
        seen = set(arr)

        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:  
                    required_sum = arr[i] + arr[j]
                    if required_sum in seen:
                        return True
    
        return False

            
        




if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
