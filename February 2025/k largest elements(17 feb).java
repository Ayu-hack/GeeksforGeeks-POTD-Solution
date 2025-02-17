class Solution {
    public ArrayList<Integer> kLargest(int[] arr, int k) {
        // Your code here
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        for(int num:arr){
            minHeap.add(num);
            if(minHeap.size()>k){
                minHeap.poll();
            }
        }
        
        ArrayList<Integer> result = new ArrayList<>(minHeap);
        result.sort(Collections.reverseOrder());
        return result;
        
    }
}
