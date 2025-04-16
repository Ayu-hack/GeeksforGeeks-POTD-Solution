class Solution {
    public void floydWarshall(int[][] dist) {
        int V = dist.length;

        // Add all vertices one by one to
        // the set of intermediate vertices.
        for (int k = 0; k < V; k++) {

            // Pick all vertices as source one by one
            for (int i = 0; i < V; i++) {

                // Pick all vertices as destination
                // for the above picked source
                for (int j = 0; j < V; j++) {

                    // If vertex k is on the shortest path
                    // from i to j, then update the value of
                    // dist[i][j]
                    if (dist[i][k] != 100000000 && dist[k][j] != 100000000 &&
                        dist[i][j] > dist[i][k] + dist[k][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
    }
}
