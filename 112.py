# Intuition
# One way to determine if there exists a root-to-leaf path in a binary tree with a given sum is to traverse the tree recursively and keep track of the current sum from the root to the current node.

# Approach
# We define a recursive function `summer` that takes a node, the target sum, and the current sum as input.
# Inside the function, we first check if the node is None. If it is, we return False.
# Otherwise, we add the value of the current node to the current sum.
# If the current node is a leaf node (i.e., it has no left or right child), we check if the current sum equals the target sum.
# If it does, we return True.
# Otherwise, we recursively call `summer` on the left and right children of the current node, passing along the target sum and the updated current sum.
# If either call returns True, we immediately return True to indicate that a root-to-leaf path with the target sum exists.
# Otherwise, we return False.
# Finally, we return the result of the initial call to `summer` with the root node and the target sum.

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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def summer(root, target, summ=0):
            if root is None:
                return False
            summ += root.val
            if not root.left and not root.right:
                if summ == target:
                    return True
            left = summer(root.left, target, summ)
            if left:
                return True
            right = summer(root.right, target, summ)
            if right:
                return True
            return False

        return summer(root, targetSum)
