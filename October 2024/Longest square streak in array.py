class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        m=-1
        nums=(set(nums))
        s=sorted(nums)
        for num in s:
            c=0
            a=num
            while a in nums:
                nums.remove(a)
                a=a**2
                c+=1

            m=max(m,c)
        return m if m>1 else -1



