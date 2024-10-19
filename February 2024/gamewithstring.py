#Given a string str of lowercase alphabets and a number k, the task is to print the minimum value of the string after removal of k characters. The value of a string is defined as the sum of squares of the count of each distinct character present in the string. Return the minimum possible required value.
#19th february
import heapq
from collections import Counter

class Solution:
    def minValue(self, s, k):
        # Step 1: Count the frequency of each character
        freq = Counter(s)
        
        # Step 2: Create a max-heap using negative frequencies
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        
        # Step 3: Remove k characters from the most frequent
        for _ in range(k):
            if max_heap:  # Ensure there are elements in the heap
                most_frequent = -heapq.heappop(max_heap)  # Get the most frequent character count
                if most_frequent > 1:  # Only reduce if there's more than 1 occurrence
                    heapq.heappush(max_heap, -(most_frequent - 1))  # Decrease the count and push back
        
        # Step 4: Calculate the minimum value
        min_value = 0
        while max_heap:
            count = -heapq.heappop(max_heap)  # Get the frequency back
            min_value += count * count  # Add the square of the count to the value
        
        return min_value

# Example Usage
if __name__ == '__main__':
    solution = Solution()
    s = "aaab"
    k = 2
    print(solution.minValue(s, k))  # Output should be the minimum possible value
