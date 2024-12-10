class Solution {
   static int minRemoval(int intervals[][]) {
        // code here
        Arrays.sort(intervals,(a,b)->Integer.compare(a[1],b[1]));
        int last = 0,ans=0,n=intervals.length;
        for(int i=1;i<n;i++){
            if(intervals[i][0]<intervals[last][1])ans++;
            else last=i;
        }
        return ans;
    }

}
