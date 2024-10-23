## **14th April 2024**: 🧩 **Problem - Xoring And Clearing**

### 📝 **Problem Statement:**
You are given an array `arr[]` of size `n`. You need to perform the following operations:

1. Calculate the **bitwise XOR** of each element in the array with its corresponding index (indices start from 0).
2. Print the resulting array after the XOR operation.
3. Set all the elements of the array to **zero**.
4. Print the updated array after all elements are set to zero.

### 🚀 **Question Link:**
[Xoring And Clearing](https://practice.geeksforgeeks.org/problems/xoring-and-clearing/0) *(Click here to view the problem)*

## Contribution By: https://github.com/Mayur-nimkande-20

## Problem Statement:
You are given an integer array `arr[]` of size `n`. The task is to apply two operations:
- **XOR operation**: Perform a bitwise XOR between each element `arr[i]` and its index `i`.
- **Clearing operation**: Set every element of the array to zero.

Your task is to print the array after both operations.

### Input:
- An integer `n` representing the size of the array.
- An integer array `arr[]` of size `n`.

### Output:
- Two lines of output:
  1. The array after performing the XOR operation on each element with its index.
  2. The array after setting all elements to zero.

### Example 1:
#### Input:
```
n = 10
arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```
#### Output:
```
1 3 1 7 1 3 1 15 1 3
0 0 0 0 0 0 0 0 0 0
```

#### Explanation:
1. First, we perform XOR on each element with its index:
   - \( arr[0] = 1 \, \oplus \, 0 = 1 \)
   - \( arr[1] = 2 \, \oplus \, 1 = 3 \)
   - \( arr[2] = 3 \, \oplus \, 2 = 1 \)
   - \( arr[3] = 4 \, \oplus \, 3 = 7 \)
   - Continue for the rest of the array...

2. After the XOR operation, the array becomes: `1 3 1 7 1 3 1 15 1 3`.
3. Now, set every element to zero: `0 0 0 0 0 0 0 0 0 0`.

### Example 2:
#### Input:
```
n = 4
arr[] = {10, 20, 30, 40}
```
#### Output:
```
10 21 28 43
0 0 0 0
```

#### Explanation:
1. Perform XOR with indices:
   - \( arr[0] = 10 \, \oplus \, 0 = 10 \)
   - \( arr[1] = 20 \, \oplus \, 1 = 21 \)
   - \( arr[2] = 30 \, \oplus \, 2 = 28 \)
   - \( arr[3] = 40 \, \oplus \, 3 = 43 \)

2. After XOR, the array becomes: `10 21 28 43`.
3. Then, set every element to zero: `0 0 0 0`.

### 💡 **Solution Overview:**

The solution involves simple operations like XOR and resetting elements to zero. Here’s a step-by-step breakdown:

### 1. **XOR Operation:**
   - Loop through each element in the array, performing a bitwise XOR between the element at index `i` and the index `i` itself.
   - Store the result in the same array.

### 2. **Clearing Operation:**
   - After the XOR operation, reset all elements of the array to zero.

### 3. **Function Definition:**
   The function `xoringAndClearing(int n, int arr[])` should:
   - Apply the XOR operation for all elements.
   - Print the array.
   - Set all elements to zero and print the array again.

### 4. **Expected Complexity:**
   - **Time Complexity**: \(O(n)\), as we iterate through the array twice—once for the XOR operation and once to set elements to zero.
   - **Space Complexity**: \(O(1)\), as we only modify the input array in place.

### **Example Walkthrough:**
Let’s take the input:
```
n = 4
arr[] = {10, 20, 30, 40}
```

- **Step 1: XOR each element with its index:**
   - \( arr[0] = 10 \, \oplus \, 0 = 10 \)
   - \( arr[1] = 20 \, \oplus \, 1 = 21 \)
   - \( arr[2] = 30 \, \oplus \, 2 = 28 \)
   - \( arr[3] = 40 \, \oplus \, 3 = 43 \)
   - The array becomes: `10 21 28 43`.

- **Step 2: Clear the array:**
   - Set all elements to zero.
   - The array becomes: `0 0 0 0`.

Both outputs are printed in sequence.