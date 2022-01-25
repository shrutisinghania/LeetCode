// { Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            int N = Integer.parseInt(read.readLine());
            
            String S[] = read.readLine().split(" ");
            int[] arr = new int[N];
            
            int D = Integer.parseInt(read.readLine());
            
            for(int i=0; i<N; i++)
                arr[i] = Integer.parseInt(S[i]);

            Solution ob = new Solution();
            System.out.println(ob.leastWeightCapacity(arr,N,D));
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution {
   static int leastWeightCapacity(int[] arr, int N, int D) {
       int start =1,end =1;
       for(int i : arr){
            start=Math.max(start,i);
            end +=i;
       }
       int weight =0;
       while(start<=end)
       {
           int mid=(start+end)/2;
           if(isPossible(arr,D,mid))
           {
               weight= mid;
               end =mid-1;
           }
           else
               start =mid+1;
       }
       return weight;
   }
   
   static boolean isPossible(int[] arr, int days,int maxWeight)
   {
       int day =1, weight= 0;
       for(int i : arr){
           weight += i;
           if(weight>maxWeight)
           {
               day++;
               weight= i;
           }
           if(day>days)
                return false;
       }
       return true;
   }
};