void rotate(vector<vector<int> >& matrix) {
    // Your code goes here
    int n = matrix[0].size();
    for(int i=0;i<n;i++){
        for(int j=i;j<n;j++){
            swap(matrix[i][j],matrix[j][i]);
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n/2;j++){
            swap(matrix[i][j],matrix[i][n-j-1]);
        }
    }
}
