class Solution {

    // Return the sum of last k nodes
    public int sumOfLastN_Nodes(Node head, int n) {
        // write code here
        Node temp = head;
        int count=0,sum=0;
        while(temp!=null){
            count++;
            temp=temp.next;
        }
        count-=n;
        temp=head;
        while(temp!=null){
            if(count==0)sum+=temp.data;
            else count--;
            temp=temp.next;
        }
        return sum;
    }

}
