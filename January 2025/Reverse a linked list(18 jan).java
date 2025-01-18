class Solution {
    Node reverseList(Node head) {
        // code here
        Node nxt=null,prev=null,cur=head;
        while(cur!=null)
        {
            nxt=cur.next;
            cur.next=prev;
            prev=cur;
            cur=nxt;
        }
        return prev;
    }
}
