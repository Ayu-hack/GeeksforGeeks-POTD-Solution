class Solution {
    // Function to search a given number in row-column sorted matrix.
    public boolean searchMatrix(int[][] mat, int x) {
        // code here
        int n=mat.length,m=mat[0].length,low=0,high=n*m-1,mid=0;
        while(low<=high){
            mid=(low+high)/2;
            int temp = mat[mid/m][mid%m];
            if(temp==x)return true;
            else if(temp<x)low=mid+1;
            else high=mid-1;
        }
        return false;
    }

}
