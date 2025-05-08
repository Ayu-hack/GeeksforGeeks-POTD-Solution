class Solution {
    Node primeList(Node head) {
        // code here
        int max=Integer.MIN_VALUE;
        Node cur=head;
        while(cur!=null){
            max=Math.max(cur.val,max);
            cur=cur.next;
        }
        boolean prime[]=new boolean[max+100];
        Arrays.fill(prime,true);
        prime[0]=false;
        prime[1]=false;
        for(int i=2;i*i<prime.length;i++){
            if(prime[i]){
                for(int j=i*i;j<prime.length;j+=i){
                    prime[j]=false;
                }
            }
        }
        cur=head;
        while(cur!=null){
            if(!prime[cur.val]){
                int left=cur.val-1;
                int right=cur.val+1;
                while(true){
                    if(left>=2 && prime[left]){
                        cur.val=left;
                        break;
                    }
                    if(right<prime.length && prime[right]){
                        cur.val=right;
                        break;
                    }
                    left--;
                    right++;
                }
            }
            cur=cur.next;
        }
        return head;
    }
}
