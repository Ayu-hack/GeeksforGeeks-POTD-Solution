class Solution {
    public int sumK(Node root, int k) {
        // code here
        Map<Integer , Integer> map = new HashMap<>();
        map.put(0 , 1);
        return get(root , map , 0 , k);
    }
    private int get(Node root , Map<Integer , Integer> map , int sum , int k){
        if(root == null) return 0;
        sum += root.data;
        int ans = 0;
        if(map.containsKey(sum - k)){
            ans += map.get(sum - k);
        }
        map.put(sum , map.getOrDefault(sum , 0) + 1);
        ans += get(root.left , map , sum , k);
        ans += get(root.right , map , sum , k);
        map.put(sum , map.get(sum) - 1);

        return ans;
    }
}
