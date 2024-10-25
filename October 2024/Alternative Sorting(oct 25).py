class Solution:
    def alternateSort(self, arr):
        arr.sort()  # Sort the array in ascending order
        result = []
        i, j = 0, len(arr) - 1
        
        # Start picking from end (largest) and beginning (smallest) alternately
        while i <= j:
            if i != j:
                result.append(arr[j])  # Add the largest element
                result.append(arr[i])  # Add the smallest element
            else:
                result.append(arr[i])  # In case of odd elements, add the middle one
            i += 1
            j -= 1
        
        return result
