// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GfG
{
    public static void main(String args[])
        {
            Scanner sc = new Scanner(System.in);
            int t = sc.nextInt();
            while(t-->0)
                {
                    String s = sc.next();
                    Solution obj = new Solution();
                    System.out.println(obj.arrangeString(s));
                }
                
        }
}
// } Driver Code Ends


//User function Template for Java

class Solution
{
    public String arrangeString(String str)
        {
            String  t =  str.replaceAll("[0-9]","");
            String sorted = "";
            int n = t.length(), sum = 0;
            int frequency [] = new int[256];
            for(int i = 0; i < 256; i++)
                frequency[i] = 0;
            for(int i = 0; i < str.length(); i++){
                char c = str.charAt(i);
                boolean isDigit = Character.isDigit(c);
                if(isDigit)
                    sum = sum + Character.getNumericValue(c);
            }
            for(int j =0 ;j<n;j++){
                char c = t.charAt(j);
                int value = (int)c;
                frequency[value]++;
            }
            for(int i =0;i<256;i++){
                for(int j = 0;j<frequency[i];j++)
                    sorted = sorted + (char)i;
            }
            return sorted+String.valueOf(sum);
        }
}
