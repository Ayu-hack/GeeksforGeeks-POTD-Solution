class Solution {

    public ArrayList<Integer> longestSubarray(int[] arr, int x) {
        // code here
        int left = 0, right = 0, maxLength = 0, startIndex = 0;
        Deque<Integer> minDeque = new LinkedList<>(); // stores indices of min elements
        Deque<Integer> maxDeque = new LinkedList<>(); // stores indices of max elements
        
        while(right<arr.length){
            // Maintain decreasing order in maxDeque
            while(!maxDeque.isEmpty() && arr[maxDeque.peekLast()] <= arr[right]){
                maxDeque.pollLast();
            }
            maxDeque.addLast(right);
            
            // Maintain increasing order in minDeque
            while(!minDeque.isEmpty() && arr[minDeque.peekLast()] >= arr[right]){
                minDeque.pollLast();
            }
            minDeque.addLast(right);
            
            // if max - min > x, move left pointer to shrink the window
            while(arr[maxDeque.peekFirst()] - arr[minDeque.peekFirst()] > x){
                left++;
                // Remove elements that are out of the new window
                if(!maxDeque.isEmpty() && maxDeque.peekFirst() < left){
                    maxDeque.pollFirst();
                }
                if(!minDeque.isEmpty() && minDeque.peekFirst() < left){
                    minDeque.pollFirst();
                }
            }
            if(right-left+1>maxLength){
                maxLength = right - left + 1;
                startIndex = left;
            }
            right++; 
        }
        ArrayList<Integer> result = new ArrayList<>();
        for(int i = startIndex; i<startIndex+maxLength; i++){
            result.add(arr[i]);
        }
        return result;
    }
}
