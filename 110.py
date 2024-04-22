# Intuition
# One way to determine if a binary tree is balanced is to recursively check if each subtree is balanced and calculate the height of each subtree.

# Approach
# We define a recursive function `height` that takes a node as input and returns a tuple containing a boolean value indicating whether the subtree rooted at that node is balanced and the height of the subtree.
# Inside the function, we first check if the node is None. If it is, we return True (indicating that the subtree is balanced) and 0 (indicating the height of the subtree is 0).
# Otherwise, we recursively call `height` on the left and right children of the current node and store the results in variables `left` and `right`, respectively.
# We then calculate whether the current subtree is balanced by checking if the absolute difference between the heights of the left and right subtrees is less than or equal to 1.
# We also check if both the left and right subtrees are balanced.
# If both conditions are met, we return True and the height of the current subtree (which is the maximum of the heights of the left and right subtrees plus 1).
# Otherwise, we return False and 0.
# Finally, we return the boolean value indicating whether the entire tree is balanced, which is the first element of the tuple returned by the initial call to `height` with the root node.

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return True, 0

            left = height(root.left)
            right = height(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return balanced, max(left[1], right[1]) + 1

        return height(root)[0]
