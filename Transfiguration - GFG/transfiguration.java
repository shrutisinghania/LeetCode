// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
class GfG
{
    public static void main(String args[])throws IOException
        {
            BufferedReader br = new BufferedReader( new InputStreamReader(System.in));
            int t = Integer.parseInt(br.readLine());
            while(t-->0)
                {
                    String arr[] = br.readLine().split(" ");
                    String A = arr[0];
                    String B = arr[1];
                    Solution obj = new Solution();
                    System.out.println(obj.transfigure (A, B));
                }
        }
}// } Driver Code Ends


//User function Template for Java

class Solution
{
    int transfigure (String A, String B)
    {
       if(A.length() != B.length()) return -1;
       int[] a = new int[256];
       int[] b = new int[256];
       for(int i = 0;i<A.length();i++){
       a[(int)A.charAt(i)]++;
       b[(int)B.charAt(i)]++;
       }
       int count = 0;
       if(Arrays.equals(a, b)){
       int i = A.length()-1; int j = B.length()-1;
       while(i>=0){
           if(A.charAt(i) ==  B.charAt(j)) j--;
           else count++;
           i--;
       }
       } else return -1;
       return count;
    }
}