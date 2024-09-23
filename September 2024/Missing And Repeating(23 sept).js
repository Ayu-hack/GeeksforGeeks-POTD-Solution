// JAVA CODE

class Solve {
    int[] findTwoElement(int arr[]) {
        // code here
        int n = arr.length;
        int ans[] = new int[2];
        for(int i=0;i<n;i++){
            int element = Math.abs(arr[i]);
            if(arr[element-1]<0)ans[0]=element;
            else arr[element-1]*=-1;
        }
        for(int i=0;i<n;i++){
            if(arr[i]>0)ans[1]=i+1;
        }
        return ans;
    }

}
