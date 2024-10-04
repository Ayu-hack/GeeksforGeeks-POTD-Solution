//JAVA CODE


class Solution {
    // Function to reverse a circular linked list
   Node deleteNode(Node head, int key) {
        // code here
        Node temp=head.next, prev=head;
        if(head.data==key){
            while(temp!=head){
                prev=temp;
                temp=temp.next;
            }
        }
        else{
            while(temp!=head && temp.data!=key){
                prev=temp;
                temp=temp.next;
            }
        }
        if(head.data==key || temp!=head)
        prev.next=temp.next;
        return head.data==key?prev.next:head;
    }
}
