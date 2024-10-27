class Solution:
    def removeDuplicates(self, arr):
        # code here 
        seen = set()  # To keep track of unique numbers
        result = []   # To store the result without duplicates
        for num in arr:
            if num not in seen:
                seen.add(num)  # Add to the set
                result.append(num)  # Add to result
        return result