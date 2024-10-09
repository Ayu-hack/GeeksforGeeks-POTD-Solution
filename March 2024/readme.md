// Kadane's algorithm

class Solution {

  // arr: input array
  // Function to find the sum of contiguous subarray with maximum sum.
  int maxSubarraySum(int[] arr) {
 
  int maxEnd = 0;
  int maxSoFar = Integer.MIN_VALUE;
  for (int i = 0; i < arr.length; i++) {          
     maxEnd = Math.max(arr[i], maxEnd + arr[i]);
     maxSoFar = Math.max(maxSoFar, maxEnd);
  }
  return maxSoFar;
  }
  public static void main(String[] args) {
        // Example with negative numbers
        int[] array1 = { -2, -3, 4, -1, -2, 1, 5, -3 };
        System.out.println("Array: [-2, -3, 4, -1, -2, 1, 5, -3]");
        System.out.println("Maximum Subarray Sum: " + maxSubarraySum(array1));
        // Example with all negative numbers
        int[] array2 = { -8, -5, -3, -9, -4 };
        System.out.println("Array: [-8, -5, -3, -9, -4]");
        System.out.println("Maximum Subarray Sum: " + maxSubarraySum(array2));
        // Example with all positive numbers
        int[] array3 = { 2, 3, 4, 5, 7 };
        System.out.println("Array: [2, 3, 4, 5, 7]");
        System.out.println("Maximum Subarray Sum: " + maxSubarraySum(array3));
    }
}
