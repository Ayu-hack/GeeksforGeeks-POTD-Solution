class Solution {
    boolean twoSum(int arr[], int target) {
        // code here
        HashMap<Integer,Integer> mm = new HashMap<>();
        for(int x:arr){
            if(mm.get(target-x)!=null)return true;
            mm.put(x,1);
        }
        return false;
    }
}
