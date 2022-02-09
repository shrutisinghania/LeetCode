// { Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main(String[] args) throws IOException
	{
	        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t =
            Integer.parseInt(br.readLine().trim()); // Inputting the testcases
        while(t-->0)
        {
            int n = Integer.parseInt(br.readLine().trim());
            Integer arr[] = new Integer[(int)(n)];
            String inputLine[] = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }
            
            Compute obj = new Compute();
            obj.sortBySetBitCount(arr, n);
            StringBuilder output = new StringBuilder();
            for(int i = 0; i < n; i++)
            output.append(arr[i] + " ");
            System.out.println(output);
            
        }
	}
}

// } Driver Code Ends


//User function Template for Java


class Compute  
{ 
   static class pair{
   int num;
   int bit;
   pair(int num,int bit){
       this.num=num;
       this.bit=bit;
   }
}
static int countbit(int n){
   int count=0;
   while(n>1){
       if(n%2==1)
          count++;
       n=n/2;   
   }
   return count+1;
}
   static void sortBySetBitCount(Integer arr[], int n)
   { 
       int[] ans= new int[n];
       for(int i=0;i<n;i++)
           ans[i]=arr[n-1-i];
       pair[] p= new pair[n];
       for(int i=0;i<n;i++)
           p[i]=new pair(ans[i],countbit(ans[i]));
       Arrays.sort(p,(a,b)->(a.bit-b.bit));
       for(int i=0;i<n;i++)
           arr[i]=p[n-1-i].num;
   } 
}
