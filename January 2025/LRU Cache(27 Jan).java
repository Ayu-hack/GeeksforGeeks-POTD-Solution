class LRUCache {
    // Constructor for initializing the cache capacity with the given value.
    static Map<Integer, Integer> cache;
    static int capacity;
    LRUCache(int cap) {
        // code here
        cache = new LinkedHashMap();
        capacity = cap;
    }
    // Function to return value corresponding to the key.
    public static int get(int key) {
        // your code here
        if(!cache.containsKey(key)){
            return -1;
        }
        int val = cache.get(key);
        cache.remove(key);
        cache.put(key, val);
        return val;
    }
    // Function for storing key-value pair.
    public static void put(int key, int value) {
        // your code here
        if(cache.containsKey(key)){
            cache.remove(key);
            cache.put(key, value);
            return;
        }
        if(cache.size() == capacity){
            int rem = -1;
            for(int i: cache.keySet()){
                rem = i;
                break;
            }
            cache.remove(rem);
        }
        
        cache.put(key, value);
    }
}
