class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        int total = grid[0].length * grid.length;
        int i = total - (k%total);
        for(int r = 0; r < grid.length; r++){
            ArrayList<Integer> tmp = new ArrayList<Integer>();
            for(int c = 0; c < grid[0].length; c++){
                int element = i++%total;
                tmp.add(grid[element/grid[0].length][element%grid[0].length]);
            }
            result.add(tmp);
        }
        
        return result; 
    }
}