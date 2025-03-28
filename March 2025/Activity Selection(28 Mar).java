class Solution {
    public int activitySelection(int[] start, int[] finish) {
        int n = start.length;
        int[][] arr = new int[n][2];
        for(int i = 0 ; i < n ; i++){
            arr[i][0] = start[i];
            arr[i][1] = finish[i];
        }
        Arrays.sort(arr, (a,b) -> a[1] - b[1]);
        int end=-1;
        int ans=0;
        for(int i = 0 ; i < n ; i++){
            if(end < arr[i][0]){
                ans++;
                end = arr[i][1];
            }
        }
        return ans;
    }
}
