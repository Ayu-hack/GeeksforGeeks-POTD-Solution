class Solution {
    public int[] matrixDiagonally(int[][] mat) {
        int n = mat.length;
        int ans[] = new int[n*n];
        int count=0, i=0, j=0;
        int upper=1;
        while(count < n*n){
            if(upper==1){
                while(i>=0 && j<n){
                    ans[count++] = mat[i][j];
                    if(j==n-1){
                        i++; break;
                    }
                    else if(i==0){
                        j++; break;
                    } 
                    i--; j++;
                }
                upper=0;
            }
            else{
                while(i<n && j>=0){
                    ans[count++] = mat[i][j];
                    if(i==n-1){
                        j++; break;
                    }
                    else if(j==0 ){
                        i++; break;
                    }
                    i++; j--;
                }
                upper=1;
            }   
        }
        return ans;
    }
}