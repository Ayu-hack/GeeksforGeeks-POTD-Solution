class Solution {
    public static String oddEven(String s) {
        // code here
        String az="abcdefghijklmnopqrstuvwxyz";
        int k,x=0,y=0;
        char arr[]=s.toCharArray();
        Map<Character, Integer> frequencyMap = new HashMap<>();
        for (char c : arr) {
            frequencyMap.put(c, frequencyMap.getOrDefault(c, 0) + 1);
        }
        for (Map.Entry<Character, Integer> entry : frequencyMap.entrySet()) {
        char c = entry.getKey();
        int v = entry.getValue();
        if ((az.indexOf(c) + 1) % 2 == 0 && v % 2 == 0) {
            x++; 
        }
        if ((az.indexOf(c) + 1) % 2 != 0 && v % 2 != 0) {
            y++;
        }
    }
        
        
        if((x+y)%2==0){
            return "EVEN";
        }
        else{
            return "ODD";
        }
        
    }
}