"""
This is a pure Python implementation for leetcode problem on geeks for geeks.
"""

class MajorityVote:
    def majorityVote(nums: list[int]) -> int:
        count = 0
        majority = 0

        for i in nums:
            if count == 0:
                majority = i

            if i == majority:
                count += 1
            else:
                count -= 1

        return majority

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # initialize to an empty list
    numbers = []

    # get the number of elements in the input list
    n = int(input("Enter number of elements in the list: "))

    # iterating till the range
    for i in range(0, n):
        ele = int(input("Enter next element in the list"))
        numbers.append(ele)


    print(MajorityVote.majorityVote(numbers))
