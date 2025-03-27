class Solution {
    static int findPlatform(int arr[], int dep[]) {
        int n = arr.length;

        // Sort arrival and departure times
        Arrays.sort(arr);
        Arrays.sort(dep);

        int platformsNeeded = 0, maxPlatforms = 0;
        int i = 0, j = 0;

        // Traverse both arrays
        while (i < n && j < n) {
            // If a train is arriving before the previous one departs
            if (arr[i] <= dep[j]) {
                platformsNeeded++; // Increase platform count
                i++;
            } else { // Train departs, release a platform
                platformsNeeded--;
                j++;
            }
            // Update maximum platforms needed
            maxPlatforms = Math.max(maxPlatforms, platformsNeeded);
        }

        return maxPlatforms;
    }
}
