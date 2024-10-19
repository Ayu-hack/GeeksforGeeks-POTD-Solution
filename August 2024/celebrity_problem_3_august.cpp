// User function template for C++

class Solution {
  public:
    // Function to find if there is a celebrity in the party or not.
    int celebrity(vector<vector<int> >& mat) {
        // code here
        int n= mat.size();
        for(int i=0;i<n;++i){
            bool knows_other = false;
            for(int j=0;j<n;++j){
                if(mat[i][j]==1 && i!=j){
                    knows_other=true;
                    break;
                }
            }
            if(!knows_other){
                bool celeb = true;
                for(int k=0;k<n;++k){
                    if(mat[k][i]==0 && k!=i){
                        celeb=false;
                        break;
                    }
                }
                if(celeb)
                    return i;
            }
        }
        return -1;
    }
};