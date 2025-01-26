class Solution {
    // Function to remove a loop in the linked list.
    public static void removeLoop(Node head) {
        // code here
        Node slow=head, fast = head, prev = head;
        while(fast!=null && fast.next!=null){
            slow = slow.next;
            prev = fast;
            fast = fast.next.next;
            if(slow == fast){
                slow = head;
                prev = prev.next;
                while(slow!=fast){
                    slow = slow.next;
                    fast=fast.next;
                    prev = prev.next;
                }
                prev.next = null;
                return;
            }
        }
    }
}
