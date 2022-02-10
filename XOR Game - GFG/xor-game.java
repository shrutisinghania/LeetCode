// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            int k = Integer.parseInt(in.readLine());
            
            Solution ob = new Solution();
            System.out.println(ob.xorCal(k));
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution{
    static int xorCal(int k){
        if(k == 1)
            return 2;
        if((k^1) == 0)
            return -1;
        int n1 = k>>1;
        int n2 = n1+1;
        if((n1^n2) == k)
            return n1;
        return -1;
    }
}