class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int[] car = new int[1001];
        for(int i =0; i < trips.length; ++i)
        {
            int j = trips[i][1]; 
            while(j != trips[i][2] )
            {
                car[j] += trips[i][0];
                if (car[j] > capacity) 
                    return false;
                j++;
            }
        }
        return true;
    }
}