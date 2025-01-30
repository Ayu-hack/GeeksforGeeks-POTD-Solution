class Solution {
    public ArrayList<ArrayList<Integer>> nQueen(int n) {
        // code here
        boolean[] col = new boolean[n];
        boolean[] ndiag = new boolean[2*n-1];
        boolean[] rdiag = new boolean[2*n-1];
        ArrayList<ArrayList<Integer>> res = new ArrayList();
        ArrayList<Integer> tmp = new ArrayList();
        solve(n, 0, col, ndiag, rdiag, res, tmp);
        return res;
    }
    static void solve(int n, int currR, boolean[] col, boolean[] ndiag, boolean[] rdiag, ArrayList<ArrayList<Integer>> res, ArrayList<Integer> tmp){
        if(currR == n){
            res.add(new ArrayList(tmp));
            return;
        }
        for(int i=0;i<n;i++){
            if(col[i]==false && ndiag[currR+i] == false && rdiag[currR-i+n-1] == false){
                tmp.add(i+1);
                col[i]=true;
                ndiag[currR+i] =true;
                rdiag[currR-i+n-1] = true;
                solve(n, currR+1, col,  ndiag, rdiag, res, tmp);
                tmp.remove(tmp.size()-1);
                col[i]=false;
                ndiag[currR+i] =false;
                rdiag[currR-i+n-1] = false;
            }
        }
    }
}
