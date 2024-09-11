
//JAVA CODE

class Solution {
    // Function to return the minimum cost of connecting the ropes.
    public long minCost(long[] arr) {
    
        // code here
        long ans = 0;
        PriorityQueue<Long> pq = new PriorityQueue<>();
        for(Long x:arr)pq.add(x);
        while(pq.size()!=1){
            long first = pq.poll();
            long second = pq.poll();
            long total = first+second;
            pq.add(total);
            ans+=total;
        }
        return ans;
    }

    
}
