// JAVA CODE

class Solution {
    int getMiddle(Node head) {
        if (head == null){ 
            return -1;
        }
        
        Node slow = head;
        Node fast = head;
        
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow.data;
    }
}
