// JAVA CODE

class Solution {
     public static long listToNum(Node node){
        long num = 0,mod=1000000007;
        while(node!=null){
            num = (num*10+node.data)%mod;
            node=node.next;
        }
        return num;
    }
    public long multiplyTwoLists(Node first, Node second) {
        // Code here
        long num1 = listToNum(first);
        long num2 = listToNum(second);
        return (num1*num2)%1000000007;
    }

}
