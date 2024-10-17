// JAVA CODE

class Solution {
    // Function to append a new node with newData at the end of a linked list
    Node[] alternatingSplitList(Node head) {
        // code here
        Node head1=null,head2=null,temp1=null,temp2=null;
        int count=0;
        while(head!=null){
            if(count%2==1){
                if(head2==null){
                    head2=head;
                    temp2=head;
                }
                else{
                    temp2.next=head;
                    temp2=temp2.next;
                }
            }
            else{
                if(head1==null){
                    head1=head;
                    temp1=head;
                }
                else{
                    temp1.next=head;
                    temp1=temp1.next;
                }
            }
            head=head.next;
            count++;
        }
        temp1.next=null;
        temp2.next=null;
        Node ans[] = new Node[2];
        ans[0]=head1;
        ans[1]=head2;
        return ans;
    }

}
