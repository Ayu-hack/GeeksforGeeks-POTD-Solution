
class Solution:
    def modifyAndRearrangeArr(self, arr):
        n = len(arr)
        for i in range(n - 1):
            if arr[i] != 0 and arr[i] == arr[i + 1]:
                arr[i] = arr[i] * 2  
                arr[i + 1] = 0 
        result = []
        for num in arr:
            if num != 0:
                result.append(num)
        result.extend([0] * (n - len(result)))
        for i in range(n):
            arr[i] = result[i]
        
        return arr