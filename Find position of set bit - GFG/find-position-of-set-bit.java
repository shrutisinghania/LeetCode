// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            int N = Integer.parseInt(read.readLine());

            Solution ob = new Solution();
            System.out.println(ob.findPosition(N));
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution {
    static int findPosition(int n) {
        int p=0;
        int count=0;
        if(n==0)
        return -1;
        String s=Integer.toBinaryString(n);
        for(int i=s.length()-1;i>=0;i--){
            if(s.charAt(i)=='1'){
                p=i;
                count++;
            }
        }
        if(count>1)
        return -1;
       return s.length()-p;
    }
};