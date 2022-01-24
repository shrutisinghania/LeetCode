// { Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            int N = Integer.parseInt(in.readLine());
            String a[] = in.readLine().trim().split("\\s+");
            int arr[] = new int[N];
            for(int i = 0;i < N;i++)
                arr[i] = Integer.parseInt(a[i]);
            
            Solution ob = new Solution();
            List<Integer> ans = new ArrayList<Integer>();
            ans = ob.nextPermutation(N, arr);
            StringBuilder out = new StringBuilder();
            for(int i = 0;i < N;i++)
                out.append(ans.get(i) + " ");
            System.out.println(out);
        }
    }
}// } Driver Code Ends


// User function Template for Java

class Solution{
    static List<Integer> nextPermutation(int N, int arr[]){
       boolean flag = false;
       for(int i=N-2;i>=0;i--){
           if(arr[i]<arr[i+1]){
               for(int j=N-1;j>=i;j--){
                   if(arr[j]>arr[i]){
                       int temp = arr[j];
                       arr[j] = arr[i];
                       arr[i] = temp;
                       reverse(arr,i+1,N-1);
                       flag = true;
                       break;
                   }
               }
           }
           if(flag==true){
               break;
           }
       }
       if(flag == false){
           reverse(arr,0,N-1);
           
       }
       
       List<Integer> ans = new ArrayList<Integer>();
       for(int a:arr){
           ans.add(a);
       }
       
       return ans;
       
   }
   
   static void reverse(int[] arr, int st, int end){
       for(int i=st,j=end;i<j;i++,j--){
           int temp = arr[i];
           arr[i] = arr[j];
           arr[j] = temp;
       }
   }
}