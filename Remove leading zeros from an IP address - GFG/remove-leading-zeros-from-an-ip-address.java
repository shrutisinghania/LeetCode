// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

public class GfG
{
    public static void main(String args[])
        {
            Scanner sc = new Scanner(System.in);
            int t = sc.nextInt();
            while(t-->0)
                {
                    String s = sc.next();
                    Solution ob = new Solution();
                    System.out.println(ob.newIPAdd(s));
                }
        }
}// } Driver Code Ends


//User function Template for Java

class Solution
{
    public String newIPAdd(String S)
   {
       String[] a = S.split("\\.");
       String myTempSt = "";
       for(int i=0;i<a.length;i++)
          myTempSt += strip(a[i])+".";
        myTempSt = myTempSt.substring(0,myTempSt.length()-1);
       return myTempSt;
   }
   
   static String strip(String st){
       String ret = "";
       boolean broke=false;
       for(int i=0;i<st.length();i++){
           String b = st.charAt(i)+"";
           if(b.equals("0") && broke==false)
               continue;
           else{
               broke = true;
               ret = ret+st.charAt(i);
           }
       }
       
       return ret.length()==0?"0":ret;
   }
}