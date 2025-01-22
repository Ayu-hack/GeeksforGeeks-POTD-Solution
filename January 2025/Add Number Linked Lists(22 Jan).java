class Solution {
    static Node addTwoLists(Node num1, Node num2) {
        // code here
        Node l1 = reverseList(num1);
        Node l2 = reverseList(num2);
        Node curr = null;
        int carry = 0;
        while(l1!=null || l2!=null || carry >0){
            int v1 = l1!=null ? l1.data : 0;
            int v2 = l2!=null ? l2.data : 0;
            int sum = v1+v2+carry;
            carry = sum/10;
            Node tmp = new Node(sum%10);
            tmp.next = curr;
            curr = tmp;
            if(l1!=null){
                l1=l1.next;
            }
            if(l2!=null){
                l2=l2.next;
            }
        }
        while(curr!=null && curr.data == 0){
            curr=curr.next;
        }
        return curr;
    
    }
    static Node reverseList(Node head) {
        // code here
        Node tmpHead = null;
        while(head!=null){
            Node nex = head.next;
            if(tmpHead == null) {
                tmpHead = head;
                tmpHead.next = null;
            }
            else {
                head.next = tmpHead;
                tmpHead = head;
            }
            head = nex;
        }
        return tmpHead;
    }
}
