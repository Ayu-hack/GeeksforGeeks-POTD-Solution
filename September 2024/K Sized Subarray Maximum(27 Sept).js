// JAVA CODE

class Solution {
    // Function to find maximum of each subarray of size k.
    public ArrayList<Integer> max_of_subarrays(int k, int arr[]) {
        // Your code here
        ArrayList<Integer> ans = new ArrayList<>();
        Deque<Integer> dq = new ArrayDeque<>();
        for(int i=0;i<arr.length;i++){
            if(dq.size()!=0 && dq.getFirst()==i-k)dq.removeFirst();
            while(dq.size()!=0 && arr[dq.getLast()]<=arr[i])dq.removeLast();
            dq.add(i);
            if(i>=k-1)ans.add(arr[dq.getFirst()]);
        }
        return ans;
    }

}
