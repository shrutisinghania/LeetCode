// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
import java.util.HashMap; 
import java.util.HashSet; 

class GFG{
	public static void main(String args[]) throws IOException { 
		Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while(t > 0){
       		int rows=sc.nextInt();
       		int columns=sc.nextInt();
			
			int matrix[][]=new int[rows][columns];
          
        	for(int i=0; i<rows;i++){            
            	for(int j=0; j<columns;j++){
                	matrix[i][j]=sc.nextInt();
            	}
         	}

			Solution x = new Solution();
			if (x.ValidCorner(matrix)) 
				System.out.println("Yes"); 
			else
				System.out.println("No"); 
			t--;
		}
	} 
}
	


// } Driver Code Ends


//User function Template for Java

public class Solution { 
	static boolean ValidCorner(int mat[][]) 
	{ 
	   int ans=0;
    HashSet<HashMap<Integer,Integer>> hs =  new HashSet<>();
    for(int i=0;i<mat[0].length;i++){
        ArrayList<Integer> al = new ArrayList<>();
        for(int j=0;j<mat.length;j++){
           if(mat[j][i]==1){
               for(int k=0;k<al.size();k++){
                   HashMap<Integer,Integer> p=new HashMap<Integer,Integer>();
                   p.put(al.get(0),j);
                   if(hs.contains(p))
                      return true;
                   else
                       hs.add(p);
               }
               al.add(j);
           }
        }
    }
    return false;
	}
}