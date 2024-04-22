# Intuition
# We can traverse the binary tree recursively and keep track of whether a node is a left leaf node or not.
# If a node is a left leaf node, we add its value to the sum. We continue this process for all nodes in the tree.

# Approach
# We define a recursive function `leftSum` that takes a node as input and returns the sum of all left leaf nodes in the subtree rooted at that node.
# Inside the function, we check if the node is None. If it is, we return 0.
# Otherwise, we initialize `left_sum` to 0. We then check if the left child of the current node exists and if it is a leaf node (i.e., it has no left or right child).
# If it is a leaf node, we add its value to `left_sum`.
# We then recursively call `leftSum` on the left and right children of the current node and add their results to `left_sum`.
# Finally, we return `left_sum`.

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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0

        def leftSum(root):
            if root is None:
                return 0

            left_sum = 0
            if root.left and root.left.left is None and root.left.right is None:
                left_sum += root.left.val

            left_sum += leftSum(root.left)
            left_sum += leftSum(root.right)
            return left_sum

        return leftSum(root)
