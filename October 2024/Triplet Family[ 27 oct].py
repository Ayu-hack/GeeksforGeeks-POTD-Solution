class Solution:
    def findTriplet(self, arr):
        # Step 1: Sort the array
        arr.sort()
        # Step 2: Iterate through each element as the target
        n = len(arr)
        for i in range(n):
            target = arr[i]
            left, right = 0, n - 1
            # Step 3: Use two pointers to find if there's a pair summing to target
            while left < right:
                # Skip if we are considering the target element
                if left == i:
                    left += 1
                elif right == i:
                    right -= 1
                else:
                    current_sum = arr[left] + arr[right]
                    
                    if current_sum == target:
                        return True  # Found a pair that sums to the target element
                    elif current_sum < target:
                        left += 1  # Move left pointer right to increase the sum
                    else:
                        right -= 1  # Move right pointer left to decrease the sum
        return False  # No triplet found that satisfies the condition

        