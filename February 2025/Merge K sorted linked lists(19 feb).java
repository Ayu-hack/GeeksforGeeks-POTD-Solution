class Solution {
    // Function to merge K sorted linked list.
    Node mergeKLists(List<Node> arr) {
        // Add your code here.
        PriorityQueue<Node> pq = new PriorityQueue<>((a,b)->a.data-b.data);
        for(Node n: arr){
            pq.add(n);
        }
        Node newHead=null, tail=null;
        while(!pq.isEmpty()){
            Node tmp = pq.poll();
            if(newHead == null){
                newHead = tmp;
                tail=tmp;
            }
            else {
                tail.next = tmp;
                tail = tmp;
            }
            if(tmp.next!=null){
                pq.add(tmp.next);
            }
        }
        return newHead;
    }
}
