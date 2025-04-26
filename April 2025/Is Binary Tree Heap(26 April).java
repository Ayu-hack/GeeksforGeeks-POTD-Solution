class Solution {
    boolean isHeap(Node tree) {
        int ndes=totcntr(tree);
        return checker(tree,1,ndes);
    }
    int totcntr(Node tree){
        if(tree==null){
            return 0;
        }
        return 1+totcntr(tree.right)+totcntr(tree.left);
    }
    boolean checker(Node tree,int ind,int lim){
        if(tree==null){
            return true;
        }
        if(ind>lim){
           return false; 
        }
        if(tree.left!=null&&tree.left.data>tree.data){
            return false;
        }
        if(tree.right!=null&&tree.right.data>tree.data){
            return false;
        }
        return checker(tree.left,ind*2,lim)&&checker(tree.right,ind*2+1,lim);
    }
}
