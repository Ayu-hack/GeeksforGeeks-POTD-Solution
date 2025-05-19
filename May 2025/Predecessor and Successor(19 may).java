class Solution {
   static Node rightMost(Node node) {
        while (node.right != null) {
            node = node.right;
        }
        return node;
    }

    static Node leftMost(Node node) {
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }

    
    static ArrayList<Node> findPreSuc(Node root, int key) {
        Node pre = null, suc = null;
        Node curr = root;

        while (curr != null) {
            if (curr.data < key) {
                pre = curr;
                curr = curr.right;
            } else if (curr.data > key) {
                suc = curr;
                curr = curr.left;
            } else {
                if (curr.left != null)
                    pre = rightMost(curr.left);
                if (curr.right != null)
                    suc = leftMost(curr.right);
                break;
            }
        }

        ArrayList<Node> result = new ArrayList<>();
        result.add(pre);
        result.add(suc);
        return result;
        
    }
}
