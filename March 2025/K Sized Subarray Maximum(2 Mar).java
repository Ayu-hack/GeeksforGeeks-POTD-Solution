class Solution {
    public ArrayList<Integer> maxOfSubarrays(int arr[], int k) {
        ArrayList<Integer> result = new ArrayList<>();
        Deque<Integer> deque = new LinkedList<>();
    for (int i = 0; i < arr.length; i++) {
        while (!deque.isEmpty() && deque.peek() < i - k + 1) {
            deque.poll();
        }
        while (!deque.isEmpty() && arr[deque.peekLast()] < arr[i]) {
            deque.pollLast();
        }
        deque.offer(i);
        if (i >= k - 1) {
            result.add(arr[deque.peek()]);
        }
    }
    return result;
    }
}
