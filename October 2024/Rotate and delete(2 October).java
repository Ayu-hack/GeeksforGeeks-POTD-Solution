// JAVA CODE

class Solution {
     public static int rotateDelete(ArrayList<Integer> arr) {
        // code here
        int n = arr.size(), temp = n/2;
        int i = 3*(temp/2);
        if(temp%2==1)i++;
        return arr.get(n-i);
    }

}
