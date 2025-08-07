import java.util.*;

class Solution {
    public boolean graphColoring(int v, int[][] edges, int m) {
        // Build adjacency list from edges
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < v; i++) adj.add(new ArrayList<>());
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]); // Undirected graph
        }

        int[] color = new int[v];  // 0 means uncolored
        return solve(0, adj, color, v, m);
    }

    private boolean solve(int node, List<List<Integer>> adj, int[] color, int v, int m) {
        if (node == v) return true;

        for (int col = 1; col <= m; col++) {
            if (isSafe(node, adj, color, col)) {
                color[node] = col;
                if (solve(node + 1, adj, color, v, m)) return true;
                color[node] = 0;  // backtrack
            }
        }

        return false;
    }

    private boolean isSafe(int node, List<List<Integer>> adj, int[] color, int col) {
        for (int neighbor : adj.get(node)) {
            if (color[neighbor] == col) return false;
        }
        return true;
    }
}
