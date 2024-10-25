class Solution {
    int minRow(int n, int m, int a[][]) {
      int minOnes = Integer.MAX_VALUE;  
        int rowIndex = 1;  
        
         for (int i = 0; i < n; i++) {
            int onesCount = 0;
            
            for (int j = 0; j < m; j++) {
                if (a[i][j] == 1) {
                    onesCount++;
                }
            }
            
            if (onesCount < minOnes) {
                minOnes = onesCount;
                rowIndex = i + 1;  
            }
        }
        
         return rowIndex;  
    }
}
