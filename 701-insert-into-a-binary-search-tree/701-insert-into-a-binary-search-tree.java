/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int v = 0;
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null)
            return new TreeNode(val);
        TreeNode n = root;
        v = val;
        insert(find(n));
        return root;
    }
    
    TreeNode find(TreeNode root)
    {
        if(root.val >= v && root.left != null)
            return find(root.left);
        else if (root.val < v && root.right != null)
            return find(root.right);
        return root;
    }
    
    void insert(TreeNode n)
    {
        TreeNode node = new TreeNode(v);
        if(n.val >= v)
        {
            n.left = node;
            return;
        }
        n.right = node;
    }
}