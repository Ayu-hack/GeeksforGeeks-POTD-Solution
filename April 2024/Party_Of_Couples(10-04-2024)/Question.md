
## **10th April 2024**: 🪜 **Problem - Find the Only Single Person in a Party of Couples**

### 📝 **Problem Statement:**
You are given an integer array `arr[]` of size `n`, representing `n` people at a party. Each person is denoted by an integer. **Couples** are represented by the same integer, meaning two people with the same number are a couple. However, there is **only one single person** in the party, meaning one number appears exactly once in the array.

Your task is to find and return the only single person in the party.

### Input:
- An integer `n` representing the size of the array.
- An integer array `arr[]` of size `n`, where each integer represents a person at the party.

### Output:
- Return the integer value of the only single person.

### Example 1:
#### Input:
```
n = 5
arr = {1, 2, 3, 2, 1}
```
#### Output:
```
3
```
#### Explanation:
Only the number `3` appears once, and all other numbers are repeated in pairs, indicating couples.

### Example 2:
#### Input:
```
n = 11
arr = {1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6}
```
#### Output:
```
4
```
#### Explanation:
All numbers except `4` have a pair, meaning `4` is the only single person in the party.

## Your Task:
You need to complete the function `findSingle(int n, int arr[])` that takes an integer `n` (the size of the array) and the array `arr[]` as input parameters and returns the integer value of the only single person.

### Expected Complexity:
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Constraints:
- \( 1 \leq n \leq 10^4 \)
- \( 1 \leq arr[i] \leq 10^6 \)

---

### 💡 **Solution Overview:**
The solution efficiently finds the single person in the party using the **XOR operator**. This approach leverages the property that when a number is XORed with itself, the result is zero (`a ^ a = 0`), and XORing a number with zero results in the number itself (`a ^ 0 = a`). By XORing all the elements in the array, all paired numbers will cancel out, leaving only the unpaired number (the single person).

### **Example:**
Let’s say `arr = {1, 2, 3, 2, 1}`:

- Start with `ans = arr[0] = 1`
- XOR operation on all elements:
  - \( ans = 1 ^ 2 = 3 \)
  - \( ans = 3 ^ 3 = 0 \)
  - \( ans = 0 ^ 2 = 2 \)
  - \( ans = 2 ^ 1 = 3 \)
- The result `3` is the single person.

---



**Contribution By:** https://github.com/Mayur-nimkande-20