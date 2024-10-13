class Pair {
    
    Node node;
    int hd;

    Pair(Node node, int hd) {
        this.node = node;
        this.hd = hd;
    }
}

class Solution {
    public ArrayList<Integer> bottomView(Node root) {
        
        ArrayList<Integer> result = new ArrayList<>();
        if (root == null) return result;

        Map<Integer, Integer> map = new TreeMap<>();
        Queue<Pair> queue = new LinkedList<>();
        queue.add(new Pair(root, 1));

        while (!queue.isEmpty()) {
            
            Pair current = queue.poll();
            Node node = current.node;
            int hd = current.hd;

            map.put(hd, node.data);

            if (node.left != null) queue.add(new Pair(node.left, hd - 1));
            if (node.right != null) queue.add(new Pair(node.right, hd + 1));
        }

        for (int value : map.values()) {
            result.add(value);
        }
        return result;
    }
}
