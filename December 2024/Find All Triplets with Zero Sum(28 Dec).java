class Solution {
     public List<List<Integer>> findTriplets(int[] arr) {
        // Your code here
        int n = arr.length;
        List<List<Integer>> ans = new ArrayList<>();
        HashMap<Integer,ArrayList<Integer>> mm = new HashMap<>();
        for(int i=0;i<n;i++){
            mm.putIfAbsent(arr[i],new ArrayList<Integer>());
            mm.get(arr[i]).add(i);
        }
        for(int i=0;i<n-2;i++){
            for(int j=i+1;j<n-1;j++){
                int rem = 0-(arr[i]+arr[j]);
                if(mm.get(rem)!=null){
                    int size=mm.get(rem).size();
                    for(int k=size-1;k>=0;k--){
                        if(mm.get(rem).get(k)<=j)break;
                        ans.add(new ArrayList<>(List.of(i,j,mm.get(rem).get(k))));
                    }
                }
            }
        }
        Collections.sort(ans,(o1, o2) -> o1.get(2).compareTo(o2.get(2)));
        return ans;
    }
}
