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
                    int n = sc.nextInt();
                    ArrayList<Integer> arr = new ArrayList<Integer>();
                    ArrayList<Integer> res = new ArrayList<Integer>();
                    for(int i=0; i<n; i++)
                        {
                            int x = sc.nextInt();
                            arr.add(x);
                        }
                    int k = sc.nextInt();
                    
                    Solution obj = new Solution();
                    res = obj.TopK(arr,k);
                    
                    for(int i=0; i<res.size();i++)
                        {
                            System.out.print(res.get(i) + " ");
                        }
                    System.out.println();    
                    
                        
                }
        }
}// } Driver Code Ends


class Solution
{
    ArrayList<Integer>TopK(ArrayList<Integer> arr, int k)
    {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<arr.size();i++)
            map.put(arr.get(i),map.getOrDefault(arr.get(i),0)+1);
       
        PriorityQueue<int[]> pq = new PriorityQueue<>((int a1[],int a2[])->{
            if(a1[1]!=a2[1])
                return a2[1]-a1[1];
            return a2[0]-a1[0];
       });
       
       for(int i=0;i<arr.size();i++)
       {
           int n=arr.get(i);
           if(map.containsKey(n))
           {
               pq.add(new int[]{n,map.get(n)});
               map.remove(n);
           }
       }
       ArrayList<Integer> list = new ArrayList<>();
       while(!pq.isEmpty() && k>0)
       {
           list.add(pq.remove()[0]);
           k--;
       }
       return list;
    }
}
