class Solution {
    static Node segregate(Node head) {
        // code here
         int zeros=0, ones=0, twos=0;
        Node head1=head;
        while(head1!=null){
            if(head1.data==0){
                zeros++;
            }
            if(head1.data==1){
                ones++;
            }
            if(head1.data==2){
                twos++;
            }
            head1=head1.next;
        }
        head1=head;
        while(head1 !=null){
            if(zeros != 0){
                head1.data=0;
                zeros--;
            }
           else if(ones != 0){
                head1.data=1;
                ones--;
            }
           else if(twos != 0){
                head1.data=2;
                twos--;
            }
            head1=head1.next;
        }
        return head;
    }
}
