class Solution {
    public static Node reverseKGroup(Node head, int k) {
        // code here
        int len = getLength(head);
        Node origH = null;
        Node origT = null, tmpH = null, tmpT=null;
        Node curr=head;
        while(len > 0){
            int j=k;
            j = Math.min(j, len);
            while(j>0){
                Node nex = curr.next;
                if(tmpH == null){
                    tmpH = curr;
                    tmpT = curr;
                }
                else {
                    curr.next = tmpH;
                    tmpH = curr;
                }
                curr=nex;
                j--;
                len--;
            }
            if(origH == null){
                origH = tmpH;
                origT = tmpT;
            }
            else {
                origT.next = tmpH;
                origT = tmpT;
            }
            tmpH = null;
            tmpT=null;
        }
        origT.next = null;
        return origH;
    }
    public static int getLength(Node head){
        int len =0;
        while(head!=null){
            len++;
            head=head.next;
        }
        return len;
    }
}
