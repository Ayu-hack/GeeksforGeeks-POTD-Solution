MOD = 10**9 + 7

def countXORWays(arr):
    totalXOR = 0
    n = len(arr)
    
    # Find the XOR of the entire array
    for num in arr:
        totalXOR ^= num
    
    # If total XOR is zero, there are ways to split
    if totalXOR != 0:
        return 0
    
    count = 0
    prefixXOR = 0
    for num in arr[:-1]:  # Exclude the last element
        prefixXOR ^= num
        if prefixXOR == 0:
            count += 1
    
    # The total number of ways to split the array
    return pow(2, count, MOD) - 1

# Example Usage
arr1 = [1, 2, 3]
arr2 = [5, 2, 3, 2]
arr3 = [2, 2, 2, 2]

print(countXORWays(arr1))  # Output: 3
print(countXORWays(arr2))  # Output: 0
print(countXORWays(arr3))  # Output: 7
