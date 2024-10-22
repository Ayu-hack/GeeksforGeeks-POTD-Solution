class Solution {
    public boolean isAdditiveSequence(String n) {
           boolean ans = false;
         int size =  n.length();
        for (int i = 1; i <  (size > 7 ? 7 : size); i++) {
            for (int j = i + 1; j <  (size > 7 ? 8 : size); j++) {
                int a = Integer.parseInt(n.substring(0, i));
                int b = Integer.parseInt(n.substring(i  , j));
                ans = helper(j, n, a, b, n.length());

                if (ans == true)
                    return true;
            }
        }
        return false;
        // code here
    }

    private   boolean helper(int i, String str, int a, int b, int n) {
        if (i >= n) {
            return true;
        }
        int sum = a + b;
        int len = String.valueOf(sum).length();

        boolean ans = false;
        if (i <= n - len) {
            int integer = Integer.parseInt(str.substring(i, i + len));
            if ((a + b) == integer) {
                ans = helper(i + len, str, b, integer, n);
            }
        }
        return ans;
       
       
    }
}
