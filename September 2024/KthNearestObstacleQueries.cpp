class Solution {
public:
    // Function that returns an array of results based on the input queries and integer k
    vector<int> resultsArray(vector<vector<int>>& queries, int k) {
        // Max heap to keep track of the top 'k' largest values (based on Manhattan distance)
        priority_queue<int> pq;
        // Vector to store the final results
        vector<int> res;

        // Iterate through each query (each query is a 2D vector containing two elements)
        for (auto i : queries) {
            // Calculate the Manhattan distance and push it into the priority queue
            pq.push(abs(i[0]) + abs(i[1]));

            // If the size of the priority queue exceeds 'k', remove the top element (the largest)
            if (pq.size() > k) {
                pq.pop();
            }

            // If the size of the priority queue is less than 'k', we append -1 to results
            if (pq.size() < k) {
                res.push_back(-1);
            } else {
                // Otherwise, we append the current top element of the priority queue (which is the kth largest distance)
                res.push_back(pq.top());
            }
        }
        // Return the results array
        return res;
    }
};
