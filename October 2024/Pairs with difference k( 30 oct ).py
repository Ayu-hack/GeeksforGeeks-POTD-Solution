class Solution:
    def countPairsWithDiffK(self, arr, k):
        unique_elements = set(arr)
        count = 0
        
        # Check for each element if element + k exists in the set
        for x in unique_elements:
            if x + k in unique_elements:
                count += 1
        
        return count
