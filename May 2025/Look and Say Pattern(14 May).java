class Solution {
    // Function to generate the look-and-say sequence
    public String countAndSay(int n) {
        if (n == 1) return "1";

        String curr = "1";

        // Start from the second term, build every term
        // terms using the previous term
        for (int i = 2; i <= n; i++) {
            StringBuilder next = new StringBuilder();
            int cnt = 1;

            for (int j = 1; j < curr.length(); j++) {

                // If same as previous, then increment
                // count
                if (curr.charAt(j) == curr.charAt(j - 1)) {
                    cnt++;

                    // If different process the previous
                    // character and its count and reset
                    // count for the current character
                } else {
                    next.append(cnt).append(curr.charAt(j - 1));
                    cnt = 1;
                }
            }

            next.append(cnt).append(curr.charAt(curr.length() - 1));
            curr = next.toString();
        }

        return curr;
    }
};
