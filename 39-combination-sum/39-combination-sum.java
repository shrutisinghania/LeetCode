class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), candidates, target, 0);
        return result;
    }
    
    private void backtrack(List<List<Integer>> result, List<Integer> r, int[] a, int sum, int strt){
        if (sum < 0)
            return;
        if (sum == 0)
        {
            result.add(new ArrayList<>(r));
            return;
        }
        for(int i = strt; i < a.length; ++i)
        {
            r.add(a[i]);
            backtrack(result, r, a, sum - a[i], i);
            r.remove(r.size() - 1);
        }
    }
}