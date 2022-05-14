class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        int[] distance = new int[n + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[k] = 0;
        //we need to run n-1 times over all edges and calculate distances
        //we run one more time to check for a negative cycle
        for (int i = 0; i < n; i++) {
            boolean anyChanged = false;
            for (int[] edge : times) {
                if (distance[edge[0]] == Integer.MAX_VALUE) 
                    continue;
                if (distance[edge[0]] + edge[2] < distance[edge[1]]) {
                    if (i == n-1) 
                        //found negative cycle
                        return -1;
                    distance[edge[1]] = distance[edge[0]] + edge[2];
                    anyChanged = true;
                }
            }
            if (!anyChanged) 
                break;
        }
        int max = Integer.MIN_VALUE;
        for (int i = 1; i <= n; i++) 
            max = Math.max(max, distance[i]);
        return max == Integer.MAX_VALUE ? -1 : max;
    }
}