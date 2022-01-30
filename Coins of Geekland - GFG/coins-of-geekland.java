// { Driver Code Starts
//Initial Template for Java

/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

class GFG {
	public static void main (String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int t = Integer.parseInt(sc.next());
		while(t-- > 0)
		{
		    int n = Integer.parseInt(sc.next());
		    int a[][] = new int[n][n];
		    
		    for(int i=0;i<n;i++)
		    {
		        for(int j=0;j<n;j++)
		        {
		            a[i][j] = Integer.parseInt(sc.next());
		        }
		    }
		    
		    int k = Integer.parseInt(sc.next());
		    Solution T = new Solution();
		    System.out.println(T.Maximum_Sum(a,n,k));
		}
	}
}// } Driver Code Ends


class Solution
{
    public int Maximum_Sum(int mat[][],int N,int k){
         if(k>N) return 0;
       int[][] b = new int[N][N];
        for(int i = 0;i<N;i++)for(int j = 0;j<N;j++){
            if(i == 0&&j==0) b[i][j] = mat[i][j];
            else if(i==0) b[i][j] = b[i][j-1] + mat[i][j];
            else if(j==0) b[i][j] = b[i-1][j] + mat[i][j];
            else b[i][j] = b[i-1][j] + b[i][j-1] + mat[i][j] -b[i-1][j-1];
        }
        if(k==N) return b[N-1][N-1];
       int sum = 0;
       for(int i = k-1;i<N;i++)for(int j = k-1;j<N;j++){
       if(i==k-1 && j == k-1) sum = b[k-1][k-1];
       else if(i == k-1) sum = Math.max(sum,b[i][j]-b[i][j-k]);
       else if(j == k-1) sum = Math.max(sum,b[i][j]-b[i-k][j]);
       else sum = Math.max(sum,b[i][j]-b[i-k][j]-b[i][j-k]+b[i-k][j-k]);
       }
       return sum;
    }
}
