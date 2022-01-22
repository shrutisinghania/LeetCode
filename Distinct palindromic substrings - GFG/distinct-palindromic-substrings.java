// { Driver Code Starts
//Initial Template for Java
import java.io.*;
import java.util.*; 
class GFG{
    public static void main(String args[]) throws IOException { 
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0){
            String str = read.readLine().trim(); 
            Solution obj = new Solution();
            int ans = obj.palindromeSubStrs(str);
            System.out.println(ans);
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution 
{ 
   int palindromeSubStrs(String str) { 
       // code here  
       int n=str.length();
       Set<String> st=new HashSet<>();
       for(int ind=0;ind<n;ind++)
       {  
           //even length palindrome
           int left=ind;
           int right=ind+1;
           String tmp="";
           while(left>=0 && right<n && str.charAt(left)==str.charAt(right))
           {
               tmp=str.charAt(left)+tmp+str.charAt(right);
               st.add(tmp);
               left--;
               right++;
           }


           //individual character
           tmp=str.charAt(ind)+"";
           st.add(tmp);
           
           //odd length palindrome
           left=ind-1;
           right=ind+1;
           while(left>=0 && right<n && str.charAt(left)==str.charAt(right))
           {
               tmp=str.charAt(left)+tmp+str.charAt(right);
               st.add(tmp);
               left--;
               right++;
           }
       }
       return st.size();
   }
} 