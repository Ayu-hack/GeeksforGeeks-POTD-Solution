// JAVA CODE

class Solution {
   public static int pairsum(int[] arr) {
        // code here
        int largest = Integer.MIN_VALUE, secondLargest = Integer.MIN_VALUE;
        for(int x:arr){
            if(x>largest){
                secondLargest=largest;
                largest=x;
            }
            else if(x>secondLargest)secondLargest=x;
        }
        return largest+secondLargest;
    }


}
