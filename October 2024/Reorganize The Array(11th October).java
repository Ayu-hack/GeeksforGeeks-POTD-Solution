class Solution {
public List<Integer> rearrange(List<Integer> arr) {
     
        // Code here
        
        HashSet<Integer> set = new HashSet<>();
        for (int i : arr) {
            set.add(i);
        }
        
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            if (set.contains(i)) {
                ans.add(i);
            } else {
                ans.add(-1);
            }
        }
        return ans;
    }
}
