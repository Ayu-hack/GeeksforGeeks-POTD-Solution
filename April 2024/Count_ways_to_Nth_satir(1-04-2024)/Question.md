## **1st April 2024**: 🪜 **Problem - Count Ways to N'th Stair**

### 📝 **Problem Statement:**
Given `n` stairs, you need to calculate the number of distinct ways a person can reach the top. The person can take either **1 stair** or **2 stairs** at a time, and **the order does not matter**.

### 🚀 **Question Link:**
[Count Ways to N'th Stair](https://www.geeksforgeeks.org/problems/count-ways-to-nth-stairorder-does-not-matter1322/1) *(Click here to view the problem)*


## Contribution By: https://github.com/Mayur-nimkande-20

## Problem Statement:
You are standing at the bottom of a staircase with **n stairs** and want to reach the top. You can climb either **1 stair** or **2 stairs** at a time. However, the **order** in which you climb does not matter. Your task is to determine how many distinct ways you can reach the top.

### Input:
- A single integer `n` representing the number of stairs.

### Output:
- Return the number of distinct ways to reach the top of the staircase.

### Example 1:
#### Input:
```
n = 4
```
#### Output:
```
3
```

#### Explanation:
You can reach the 4th stair in **3 distinct ways**:
- **1 + 1 + 1 + 1** (all steps of size 1)
- **1 + 1 + 2** (a mix of steps of size 1 and 2)
- **2 + 2** (all steps of size 2)

Note: Different permutations of the same combination (e.g., `{1,1,2}` vs. `{1,2,1}`) are considered the same.

### Example 2:
#### Input:
```
n = 5
```
#### Output:
```
3
```

#### Explanation:
You can reach the 5th stair in **3 distinct ways**:
- **1 + 1 + 1 + 1 + 1** (all steps of size 1)
- **1 + 1 + 1 + 2** (a mix of steps of size 1 and 2)
- **1 + 2 + 2** (more steps of size 2)

## Your Task:
Complete the function `countWays(n)` that takes an integer `n` and returns the total number of distinct ways to reach the top.

### Expected Complexity:
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

## Constraints:
- \(1 \leq N \leq 10^6\)



### 💡 **Solution Overview:**
The solution efficiently counts the distinct ways to climb the stairs using dynamic programming. The logic leverages the fact that for even stairs, there are extra combinations when compared to odd stairs.

### 1. **Function Definition:**
   The function `countWays(int n)` takes an integer `n` (the number of stairs) as an input and returns the number of distinct ways to reach the top of the stairs.

### 2. **What is `v[]`?**
   - `v` is a vector (similar to an array) of size `n+1`. It is used to store the number of ways to reach each stair.
   - The vector's purpose is to keep track of the number of ways to reach every stair from 0 to `n`. 
   - We initialize two elements of the vector:
     - `v[0] = 1`: There's **1 way** to stay at the ground (do nothing).
     - `v[1] = 1`: There's **1 way** to reach the first stair (only by taking one 1-step).

### 3. **Iterating Through Stairs:**
   - The function then loops from stair 2 to `n`, updating `v[i]`, which stores the number of distinct ways to reach the `i`-th stair.

### 4. **Logic for Even and Odd Stairs:**
   - If the current stair `i` is **even** (i.e., divisible by 2), it means the person can reach this stair by taking steps in two ways:
     1. Taking `1-step` stairs (just like odd staircases).
     2. Taking pairs of `2-step` stairs.
     - For even stairs, we increment the number of ways by 1 (to account for the additional "all 2-steps" combination).
     - `v[i] = v[i-1] + 1` handles this by adding one more combination to the previous stair's count.
   
   - If the current stair `i` is **odd**, the number of distinct ways remains the same as for the previous stair (`v[i] = v[i-1]`). This is because, in terms of distinct combinations, the additional stair can only be reached by adding one more 1-step, and no new unique combinations are possible.

### 5. **Result:**
   - After the loop finishes, `v[n]` holds the total number of distinct ways to reach the top of the staircase with `n` stairs.

### **Example:**
Let’s say `n = 4` (4 stairs):

- `v[0] = 1` → There's 1 way to stay at the ground.
- `v[1] = 1` → There's 1 way to reach the 1st stair (take a single 1-step).
- `v[2] = v[1] + 1 = 2` → For 2 stairs, you can either take two 1-steps, or one 2-step.
- `v[3] = v[2] = 2` → For 3 stairs, the combinations remain the same as for 2 stairs (you can't create a new unique way using 1-step and 2-step combinations).
- `v[4] = v[3] + 1 = 3` → For 4 stairs, you add another unique way: taking two 2-steps (2+2), so there are 3 ways total.

