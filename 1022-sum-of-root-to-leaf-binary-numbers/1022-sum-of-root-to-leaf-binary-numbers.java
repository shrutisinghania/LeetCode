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
    int sum = 0;
    public int sumRootToLeaf(TreeNode root) {
        sumNodes(root, 0);
        return sum;
    }
    
    void sumNodes (TreeNode r, int s)
    {
        if (r == null)
            return;
        s = s*2 + r.val;
        if (r.left == null && r.right == null)
        {
            sum += s;
            return;
        }
        if (r.left != null)
            sumNodes(r.left, s);
        if (r.right != null)
            sumNodes(r.right, s);
    }
}