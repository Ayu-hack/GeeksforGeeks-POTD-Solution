class Solution {
public:
    int pairsViolatingBST(int n, Node *root) {
        vector<int> inorderTraversal;
        inorder(root, inorderTraversal);
        vector<int> temp(n);
        return mergeSort(0, n - 1, inorderTraversal, temp);
    }

private:
    void inorder(Node* root, vector<int>& inorderTraversal) {
        if (root) {
            inorder(root->left, inorderTraversal);
            inorderTraversal.push_back(root->data);
            inorder(root->right, inorderTraversal);
        }
    }

    int merge(int low, int mid, int high, vector<int>& arr, vector<int>& output) {
        int i = low, j = mid + 1;
        int k = low;
        int inversions = 0;

        while (i <= mid && j <= high) {
            if (arr[i] <= arr[j])
                output[k++] = arr[i++];
            else {
                output[k++] = arr[j++];
                inversions += (mid - i + 1);
            }
        }

        while (i <= mid)
            output[k++] = arr[i++];
        while (j <= high)
            output[k++] = arr[j++];

        for (int i = low; i <= high; ++i)
            arr[i] = output[i];

        return inversions;
    }

    int mergeSort(int low, int high, vector<int>& arr, vector<int>& output) {
        int inversions = 0;

        if (low < high) {
            int mid = (low + high) / 2;

            inversions += mergeSort(low, mid, arr, output);
            inversions += mergeSort(mid + 1, high, arr, output);
            inversions += merge(low, mid, high, arr, output);
        }

        return inversions;
    }
};