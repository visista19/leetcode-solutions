import java.util.*;
class Pair{
    int first;
    int second;
    Pair(int first, int second){
        this.first=first;
        this.second=second;
    }
}
class Solution {
    public boolean detectCycle(int src, int V, ArrayList<ArrayList<Integer>> adj, boolean[] vis){
        vis[src]=true;
        Queue<Pair>q=new LinkedList<>();
        q.add(new Pair(src,-1));
        while(!q.isEmpty()){
        int node = q.peek().first;
        int parent =q.peek().second;
        q.remove();
        for(int adjN : adj.get(node)){
            if(vis[adjN]==false){
                vis[adjN]=true;
                q.add(new Pair(adjN,node));
            }
            else if(parent!=adjN){
                return true;
            }
        }
    }
        return false;
    }
    public boolean isCycle(int V, int[][] edges) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for(int i=0;i<=V;i++){
            adj.add(new ArrayList<Integer>());
        }
        for(int[] edge: edges){
            int u=edge[0];
            int v=edge[1];
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        boolean[] vis = new boolean[V];
        for(int i=0;i<V;i++) vis[i]=false;
        for(int i=0;i<V;i++){
            if(vis[i]==false){
                if(detectCycle(i, V, adj, vis)) return true;
            }
        }
        return false;
        
    }
}