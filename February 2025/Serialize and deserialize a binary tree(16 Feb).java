class Tree {
    // Function to serialize a tree and return a list containing nodes of tree.
    public ArrayList<Integer> serialize(Node root) {
        ArrayList<Integer> arr = new ArrayList<>();
        serialize(root, arr);
        return arr;
    }
    
    void serialize(Node root, ArrayList<Integer> arr){
        if(root == null){
            arr.add(-1);
            return;
        }
        arr.add(root.data);
        serialize(root.left, arr);
        serialize(root.right, arr);
    }

    // Function to deserialize a list and construct the tree.
    public Node deSerialize(ArrayList<Integer> arr) {
        int []index = new int[1];
        return deSerialize(arr, index);
    }
    Node deSerialize(ArrayList<Integer>arr, int[] index){
        if (arr.get(index[0]) == -1){
            ++index[0];
            return null;
        }
        Node newNode = new Node(arr.get(index[0]));
        ++index[0];
        newNode.left = deSerialize(arr, index);
        newNode.right = deSerialize(arr, index);
        return newNode;
    }
};
