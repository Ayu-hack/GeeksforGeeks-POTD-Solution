class Solution {
  public int maxDistance(int[] nums) {

    // code here
    
      int maxDistanceElements = -1;
      HashMap<Integer, Integer> map = new HashMap<>();
    
      for (int i = 0; i < nums.length; i++) {
          if (map.containsKey(nums[i])) {
              maxDistanceElements = Math.max(maxDistanceElements, i - map.get(nums[i]));
          } else {
              map.put(nums[i], i);
          }
      }
    return maxDistanceElements;
  }
}
