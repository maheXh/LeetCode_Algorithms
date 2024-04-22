# Intuition
# One approach to find the minimum depth of a binary tree is to traverse the tree recursively and keep track of the depth of each node.

# Approach
# We define a recursive function `depth` that takes a node as input and returns the depth of the subtree rooted at that node.
# Inside the function, we first check if the node is None. If it is, we return 0 to indicate that the depth is 0.
# Otherwise, we recursively call `depth` on the left and right children of the current node and store the results in variables `left` and `right`, respectively.
# We then check if either `left` or `right` is 0, which indicates that one of the children is None (i.e., the current node is a leaf node).
# In this case, we return the maximum of `left` and `right` plus 1 to account for the current node.
# Otherwise, we return the minimum of `left` and `right` plus 1 to find the minimum depth of the subtree.
# Finally, we return the result of the initial call to `depth` with the root node.

# Complexity
# Time complexity: O(n), where n is the number of nodes in the binary tree. We visit each node once.
# Space complexity: O(h), where h is the height of the binary tree. This represents the space used by the recursion stack.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if root is None:
                return 0
            left, right = depth(root.left), depth(root.right)

            if left == 0:
                return right + 1
            if right == 0:
                return left + 1

            return min(left, right) + 1

        return depth(root)
