class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int i = 0, ans = 0, j = people.length - 1;
        while(i <= j)
        {
            ans++;
            if(people[i] + people[j] <= limit)
                i++;
            j--;
        }
        return ans;
    }
}