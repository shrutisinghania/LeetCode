// { Driver Code Starts
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
            int n = Integer.parseInt(read.readLine().trim());
            String arr[] = read.readLine().trim().split(" ");

            Solution ob = new Solution();
            System.out.println(ob.longestCommonPrefix(arr, n));
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution{
    String longestCommonPrefix(String arr[], int n){
        int len = arr[0].length();
        String s = arr[0];
        for(int i = 1; i < arr.length; ++i)
        {
            len = prefix(arr[i], s, len);
            if (len == 0)
                return "-1";
            len = Math.min(len, arr[i].length());
            s = s.substring(0,len);
        }
        return s;
    }
    
    int prefix(String s1, String s2, int end)
    {
        for(int i = 0; i < end; ++i)
        {
            if(i >= s1.length() || i >= s2.length() || s1.charAt(i)!=s2.charAt(i))
                return i;
        }
        return end;
    }
}