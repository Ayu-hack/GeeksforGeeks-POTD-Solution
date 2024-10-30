class Solution:
    def countPairsWithDiffK(self,arr, k):
	    count = 0
        seen = {}

        for number in arr:
            if (number - k) in seen:
                count += seen[number - k]  
            if (number + k) in seen:
                count += seen[number + k]  
        
            if number in seen:
                seen[number] += 1
            else:
                seen[number] = 1

        return count


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

