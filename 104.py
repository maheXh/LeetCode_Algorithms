# Intuition
# One way to find the maximum depth of a binary tree is to traverse the tree recursively and calculate the height of each subtree.

# Approach
# We define a recursive function `height` that takes a node as input and returns the height of the subtree rooted at that node.
# Inside the function, we first check if the node is None. If it is, we return 0 to indicate that the height of the subtree is 0.
# Otherwise, we recursively call `height` on the left and right children of the current node and store the results in variables `left` and `right`, respectively.
# We then return the maximum of `left` and `right` plus 1 to find the height of the subtree rooted at the current node.
# Finally, we return the result of the initial call to `height` with the root node.

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root is None:
                return 0
            left = height(root.left)
            right = height(root.right)

            return max(left, right) + 1

        return height(root)
