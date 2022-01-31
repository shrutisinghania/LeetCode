// { Driver Code Starts
//Initial Template for Java

//Initial Template for Java

import java.util.*;
import java.io.*;

class Node {
    int data;
    Node left;
    Node right;
    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
} class GfG {
    public static Node buildTree(String str) {

        if (str.length() == 0 || str.charAt(0) == 'N') {
            return null;
        }

        String ip[] = str.split(" ");
        // Create the root of the tree
        Node root = new Node(Integer.parseInt(ip[0]));
        // Push the root to the queue

        Queue<Node> queue = new LinkedList<>();

        queue.add(root);
        // Starting from the second element

        int i = 1;
        while (queue.size() > 0 && i < ip.length) {

            // Get and remove the front of the queue
            Node currNode = queue.peek();
            queue.remove();

            // Get the current node's value from the string
            String currVal = ip[i];

            // If the left child is not null
            if (!currVal.equals("N")) {

                // Create the left child for the current node
                currNode.left = new Node(Integer.parseInt(currVal));
                // Push it to the queue
                queue.add(currNode.left);
            }

            // For the right child
            i++;
            if (i >= ip.length) break;

            currVal = ip[i];

            // If the right child is not null
            if (!currVal.equals("N")) {

                // Create the right child for the current node
                currNode.right = new Node(Integer.parseInt(currVal));

                // Push it to the queue
                queue.add(currNode.right);
            }
            i++;
        }

        return root;
    }
    
    public static Node point(Node root, int n)
    {
        if(root == null)
            return null;
            
        if(root.data == n)
            return root;
            
        Node l = point(root.left, n);
        if(l!=null && l.data==n)
            return l;
            
        Node r= point(root.right, n);
        return r;
        
        
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine().trim());

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());
            String s = br.readLine();
            Node root = buildTree(s);
            
            Node p = point(root,n);
            
            Solution ob=new Solution();
            ArrayList<Integer> ans= ob.printCousins(root, p);
            
            for(int i=0;i<ans.size();i++)
            {
                    System.out.print(ans.get(i)+" ");
    
            }
            
            System.out.println();
            
        }
    }
}// } Driver Code Ends


//User function Template for Java

/*
class Node {
    int data;
    Node left;
    Node right;
    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
} */

class Solution
{
    public static ArrayList<Integer> printCousins(Node root, Node node_to_find)
    {
        int dep=getDepth(node_to_find,root);
       if(dep==Integer.MAX_VALUE)return new ArrayList<Integer>();
       ArrayList<Integer> ans=new ArrayList<>();
       helper(ans,root,dep,node_to_find);
       if(ans.size()==0)ans.add(-1);
       return ans;
   }
   public static void helper(ArrayList<Integer> ans,Node root,int dep,Node node){
       if(root==null)return;
       if(dep==1){
           if(root.left!=null&&root.left==node)return ;
           if(root.right!=null&&root.right==node)return ;
           if(root.left!=null)ans.add(root.left.data);
           if(root.right!=null)ans.add(root.right.data);
           return;
       }
       helper(ans,root.left,dep-1,node);
       helper(ans,root.right,dep-1,node);
       
       
   }
   public static int getDepth(Node node,Node root){
       if(root==null)return Integer.MAX_VALUE;
       if(node==root)return 0;
       // return Math.min(getDepth(node,root.left),getDepth(node,root.right));
       int left=getDepth(node,root.left);
       if(left!=Integer.MAX_VALUE)return left+1;
       int right=getDepth(node,root.right);
       if(right!=Integer.MAX_VALUE)return right+1;
       return Integer.MAX_VALUE;
   }
}