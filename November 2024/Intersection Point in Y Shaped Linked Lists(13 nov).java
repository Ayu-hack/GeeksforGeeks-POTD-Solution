class Intersect {
    // Function to find intersection point in Y shaped Linked Lists.
    static int findLength(Node head){
        Node temp=head;
        int len=0;
        while(temp!=null){
            len++;
            temp=temp.next;
        }
        return len;
    }
    // Function to find intersection point in Y shaped Linked Lists.
    int intersectPoint(Node head1, Node head2) {
        // code here
        int len1=findLength(head1);
        int len2=findLength(head2);
        while(len1>len2){
            head1=head1.next;
            len1--;
        }
        while(len2>len1){
            head2=head2.next;
            len2--;
        }
        while(head1!=null && head2!=null){
            if(head1==head2)return head1.data;
            head1=head1.next;
            head2=head2.next;
        }
        return -1;
    }
}
