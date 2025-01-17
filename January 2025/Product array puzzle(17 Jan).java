class Solution {
    public static int[] productExceptSelf(int arr[]) {
        // code here
        int n = arr.length, totalProd = 1, zeroCnt = 0;
        int[] res = new int[n];
        for(int i: arr){
            if(i==0){
                zeroCnt++;
            }
            else{
                totalProd*=i;
            } 
        }
        if(zeroCnt > 1){
            return res;
        }
        if(zeroCnt == 1){
            for(int i=0;i<n;i++){
                if(arr[i]==0){
                    res[i]=totalProd;
                }
            }
            return res;
        }
        for(int i=0;i<n;i++){
            res[i] = totalProd/arr[i];
        }
        return res;
    }
}
