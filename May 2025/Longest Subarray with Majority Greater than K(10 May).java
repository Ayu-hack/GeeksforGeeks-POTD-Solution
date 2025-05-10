class Solution {
    int longestSubarray(int[] arr, int k) {
    Map<Integer, Integer> prefixMap = new HashMap<>();
    prefixMap.put(0, -1);
    int prefixSum = 0, maxLength = 0;
    
    for (int i = 0; i < arr.length; i++) {
        prefixSum += (arr[i] > k) ? 1 : -1;
        
        if (prefixSum > 0) {
            maxLength = i + 1;
        } else {
            if (prefixMap.containsKey(prefixSum - 1)) {
                maxLength = Math.max(maxLength, i - prefixMap.get(prefixSum - 1));
            }
        }
        
        prefixMap.putIfAbsent(prefixSum, i);
    }
    
    return maxLength;
}
}
