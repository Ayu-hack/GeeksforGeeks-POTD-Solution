class Solution {
   ArrayList<Integer> removeDuplicate(int arr[]) {
        // code here
        int mm[] = new int[101];
        Arrays.fill(mm,0);
        ArrayList<Integer> ans = new ArrayList<>();
        for(int x:arr){
            if(mm[x]==0){
                ans.add(x);
                mm[x]=1;
            }
        }
        return ans;
    }

}
