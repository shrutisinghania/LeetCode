class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int[] car = new int[1001];
        int maxDist = 0, j = 0;
        for(int i =0; i < trips.length; ++i)
        {
            car[trips[i][1]] += trips[i][0];
            car[trips[i][2]] -= trips[i][0];
            maxDist = Math.max(maxDist,trips[i][2]); 
                       
        }
        for(int i = 0; i < maxDist; ++i)
        {
            j += car[i];
            if (j > capacity) 
                return false;
        }
        return true;
    }
}