class Solution {
    
    public void threeWayPartition(int array[], int a, int b) {
        int start = 0, end = array.length - 1;
        
        for (int i = 0; i <= end;) {
            if (array[i] < a) {
                int temp = array[i];
                array[i] = array[start];
                array[start] = temp;
                start++;
                i++;
            } else if (array[i] > b) {
                int temp = array[i];
                array[i] = array[end];
                array[end] = temp;
                end--; // Do not increment i here, as the new element at array[i] needs to be checked.
            } else {
                i++;
            }
        }
    }
}
