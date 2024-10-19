#4 january
#Given an array of integers arr[] of length N, every element appears thrice except for one which occurs once.
#Find that element which occurs once.
class Solution:
    def singleElement(self, arr, N):
        """
        This function finds the element that appears only once in the given array.
        
        Parameters:
        arr (list): The input array containing integers.
        N (int): The length of the input array.
    
        Returns:
        int: The element that appears only once in the array.
        """
        
        # Initialize ones and twos
        ones = 0
        twos = 0

        # Iterate through the array
        for num in arr:
            # Update twos
            twos |= ones & num
            # Update ones
            ones ^= num
            # Calculate threes (common bits in ones and twos)
            threes = ones & twos
            # Remove common bits from ones and twos
            ones &= ~threes
            twos &= ~threes

        return ones

# Example usage
if __name__ == "__main__":
    solution = Solution()
    arr = [1, 10, 1, 1]
    N = len(arr)
    result = solution.singleElement(arr, N)
    print(result)  # Output only the result
