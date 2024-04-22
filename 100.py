# Intuition
# One approach to determine if two binary trees are the same is to traverse both trees simultaneously and compare the values of corresponding nodes.

# Approach
# We define a recursive function `check` that takes two nodes as input and returns True if the subtrees rooted at these nodes are the same, and False otherwise.
# Inside the function, we first check if both nodes are None. If they are, we return True to indicate that the subtrees are the same.
# If one of the nodes is None while the other is not, we return False, as the subtrees cannot be the same.
# If both nodes are not None, we check if their values are equal. If they are not, we return False, as the subtrees cannot be the same.
# Otherwise, we recursively call `check` on the left child of the first node and the left child of the second node, and on the right child of the first node and the right child of the second node.
# We return the result of the logical AND operation between the two recursive calls.
# Finally, we return the result of the initial call to `check` with the roots of the two trees.

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return check(p.left, q.left) and check(p.right, q.right)

        return check(p, q)
