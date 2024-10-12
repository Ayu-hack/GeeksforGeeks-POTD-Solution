class Solution {
    // Function to find the maximum number of meetings that can
    // be performed in a meeting room.
    public int maxMeetings(int n, int start[], int end[]) {
        
        // add your code here
        
        int[][] meetings = new int[n][2];
        for (int i = 0; i < n; i++) {
            meetings[i][0] = start[i];
            meetings[i][1] = end[i];
        }

        Arrays.sort(meetings, Comparator.comparingInt(a -> a[1]));

        int meetingsCount = 1;
        int time = meetings[0][1];

        for (int i = 1; i < n; i++) {
            if (meetings[i][0] > time) {
                meetingsCount++;
                time = meetings[i][1];
            }
        }
        return meetingsCount;
    }
}
