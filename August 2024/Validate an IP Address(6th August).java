class Solution {
    public boolean isValid(String s) {
        // Write your code here
        String[] ip = s.split("\\.");
        
        if (ip.length != 4) {
            return false;
        }
        
        for (String i : ip) {
            if (i == null || i.length() == 0) {
                return false;
            }
            // removing leading zeros
            if (i.length() > 1 && i.charAt(0) == '0') {
                return false;
            }
            if (Character.isDigit(i.charAt(0))) {
                if (Integer.parseInt(i) >= 0 && Integer.parseInt(i) <= 255) {
                    continue;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
        return true;
    }
}
