// { Driver Code Starts
//Initial Template for Java

//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        
        while(t-- > 0)
        {
            String str[] = read.readLine().trim().split("\\s+");
            int r = Integer.parseInt(str[0]);
            int c = Integer.parseInt(str[1]);
            int matrix[][] = new int[r][c];
            
            for(int i = 0; i < r; i++)
            {
                int k = 0;
                str = read.readLine().trim().split("\\s+");
                for(int j = 0; j < c; j++){
                  matrix[i][j] = Integer.parseInt(str[k]);
                  k++;
                }
            }
            Solution obj = new Solution();
            int[] p = obj.endPoints(matrix,r,c);
            System.out.print("(" +  p[0]+ ", " +  p[1]+ ")" +"\n");
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution{
    static int [] endPoints(int [][]arr, int m, int n){
        int[] a=new int[2];
        int ex1=-1,ex2=-1;
        if(n==1 && arr[0][0]==0)
        return a;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                
                     check(arr,m,n,i,j,1,ex1,ex2,a); 
                     if(a[0]!=-1)
                     return a;
                     
                
            }
        }
           //right--1, left---2,up----3,down---4 
           a[0]=m-1;
           a[1]=n-1;
        return a;
        
    }
    static public void check(int [][]arr,int m,int n,int i,int j,int dir,int ex1,int ex2,int a[])
    {
        if(i>=0 && i<m && j<n && j>=0)
           {
               if(arr[i][j]==1)
               {
                    arr[i][j]=0;
                    if(dir==1)
                    check(arr,m,n,i+1,j,4,i,j,a);
                    else if(dir==2)
                    check(arr,m,n,i-1,j,3,i,j,a);
                    else if(dir==3)
                    check(arr,m,n,i,j+1,1,i,j,a);
                    else if(dir==4)
                    check(arr,m,n,i,j-1,2,i,j,a);
               }
               else
               {
                 if(dir==1)
                    check(arr,m,n,i,j+1,1,i,j,a);
                    else if(dir==2)
                    check(arr,m,n,i,j-1,2,i,j,a);
                    else if(dir==3)
                    check(arr,m,n,i-1,j,3,i,j,a);
                    else if(dir==4)
                    check(arr,m,n,i+1,j,4,i,j,a); 
               }
                    
                
            }
            else
            {
                a[0]=ex1;
                a[1]=ex2;
                return;
            }
        }
}