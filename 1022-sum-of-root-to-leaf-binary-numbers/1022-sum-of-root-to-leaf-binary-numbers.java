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
    public int sumRootToLeaf(TreeNode root) {
        int r = 0, cur = 0;
        Deque<Pair<TreeNode, Integer>> s = new ArrayDeque();
        s.push(new Pair(root, cur));
        while(!s.isEmpty())
        {
            Pair<TreeNode, Integer> p = s.pop();
            root = p.getKey();
            cur = p.getValue();
            if(root != null)
            {
                cur = (cur << 1) | root.val;
                if(root.left == null && root.right == null)
                    r += cur;
                else
                {
                    s.push(new Pair(root.right, cur));
                    s.push(new Pair(root.left, cur));
                }
            }
        }
        return r;
    }
}