// { Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {
            String[] s = br.readLine().trim().split(" ");
            int n = Integer.parseInt(s[0]);
            int m = Integer.parseInt(s[1]);
            char[][] grid = new char[n][m];
            for (int i = 0; i < n; i++) {
                String[] S = br.readLine().trim().split(" ");
                for (int j = 0; j < m; j++) {
                    grid[i][j] = S[j].charAt(0);
                }
            }
            Solution obj = new Solution();
            int ans = obj.numIslands(grid);
            System.out.println(ans);
        }
    }
}// } Driver Code Ends


class Solution {
    public int numIslands(char[][] grid) {
        
        if(grid.length=='0')
            return 0;
        int island=0;
        int r=grid.length;
        int c=grid[0].length;
        
        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                if(grid[i][j]=='1'){
                    dfsCall(grid, i, j);
                    island++;
                }
            }
        }
        return island;
    }
    void dfsCall(char[][] grid, int i, int j){
        if(i<0 || j<0 || i>grid.length-1 || j>grid[0].length-1 || (grid[i][j]=='0'))
            return; // at out of bound case || water part
        grid[i][j]='0';
        dfsCall(grid,i+1,j);
        dfsCall(grid,i-1,j);
        dfsCall(grid,i+1,j+1); // diagonal
        dfsCall(grid,i-1,j-1); // diagonal
        dfsCall(grid,i-1,j+1);// diagonal
        dfsCall(grid,i+1,j-1); // diagonal
        dfsCall(grid,i,j+1);
        dfsCall(grid,i,j-1);
    }
}