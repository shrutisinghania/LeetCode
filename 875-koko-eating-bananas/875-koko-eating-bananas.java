class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int right = 1, left = 1;
        for(int p : piles)
            right = (p > right) ? p : right;
         while (left < right)
         {
             int middle = (left + right) / 2;
             int hrs = 0;
             for (int p : piles)
                 hrs += Math.ceil((double) p / middle);
             if (hrs <= h)
                 right = middle;
             else
                 left = middle + 1;
         }
        return right;
    }
}