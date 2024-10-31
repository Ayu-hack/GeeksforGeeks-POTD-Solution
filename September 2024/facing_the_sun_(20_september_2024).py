class Solution:
    def countBuildings(self, height):
        ans = 1
        mx = height[0]
        
        for x in height:
            if x > mx:
                mx = x
                ans += 1
                
        return ans
