// { Driver Code Starts
//Initial Template for Java
import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0)
        {
            int N = sc.nextInt();
			
            Solution ob = new Solution();
            ArrayList<Integer> ans = ob.increasingNumbers(N);
            for(int num : ans){
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}
// } Driver Code Ends


//User function Template for Java
class Solution{
    
    static ArrayList<Integer> increasingNumbers(int N){
        ArrayList<Integer> a = new ArrayList<Integer>();
        if(N == 1)
            a.add(0);
        increasingNo(a, N, 0, new String());
        return a;
    }
    
    static void increasingNo(ArrayList<Integer> a, int n, int cur, String s){
        if(s.length()==n)
        {
            a.add(Integer.parseInt(s));
            return;
        }
        for(int i = cur+1; i<=9; ++i)
            increasingNo(a, n, i, (s+Integer.toString(i)));
    }
}