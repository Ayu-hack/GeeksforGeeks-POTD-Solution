class Solution {
    public int findMaxDiff(int[] arr) {
        // code here
        int n = arr.length;
        int ls [] = new int [n];
        int rs [] = new int [n];
        Stack<Integer> st = new Stack<>();
        int i =n-1;
        while(i >=0 ){
            if(st.size()==0){
                st.push(arr[i]);
                rs[i]=0;
            }else{
                if(st.peek() < arr[i] ){
                    rs[i] = st.peek();
                    st.push(arr[i]);
                }else{
                    while(st.size()!=0 && st.peek()>= arr[i]){
                        int val = st.pop();
                    }
                    if(st.size()==0) {
                        st.push(arr[i]);
                        rs[i]=0;
                    }
                    if(st.peek() < arr[i] ){
                    rs[i] = st.peek();
                    st.push(arr[i]);
                    }
                }
            }
            i--;
        }
        
        while(st.size()>0){ int val = st.pop();}
        
        i =0 ;
        while(i<n){
             if(st.size()==0){
                st.push(arr[i]);
                ls[i]=0;
            }else{
                if(st.peek() < arr[i] ){
                    ls[i] = st.peek();
                    st.push(arr[i]);
                }else{
                    while(st.size()!=0 && st.peek()>= arr[i]){
                        int val = st.pop();
                    }
                    if(st.size()==0) {
                        st.push(arr[i]);
                        ls[i]=0;
                    }
                    if(st.peek() < arr[i] ){
                    ls[i] = st.peek();
                    st.push(arr[i]);
                    }
                }
            }
            i++;
        }
        
        int max =0;
        for( i=0;i<n;i++){
        //   if(ls[i]!=0 && rs[i]!=0){
           
               max = Math.max(max, Math.abs(ls[i]-rs[i]));
                // System.out.println(ls[i] +"   "+ rs[i]);
        //   } 
        }
        //  System.out.println(ls[n-1]);
       return max; 
    }
}
