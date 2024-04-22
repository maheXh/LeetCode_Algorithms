# Intuition
# One intuitive approach to invert a binary tree is to traverse the tree recursively and swap the left and right children of each node.

# Approach
# We define a recursive function `swapper` that takes a node as input.
# Inside the function, we first check if the node is None. If it is, we return.
# Otherwise, we swap the left and right children of the current node using a temporary variable.
# Then, we recursively call `swapper` on the left and right children of the current node.
# Finally, we return the root node of the inverted binary tree.

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swapper(root):
            if root is None:
                return
            root.left, root.right = root.right, root.left
            swapper(root.left)
            swapper(root.right)

        swapper(root)
        return root
