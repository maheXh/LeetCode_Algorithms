# Intuition
# One common approach to traverse a binary tree is the inorder traversal, which visits nodes in the order: left, root, right.

# Approach
# We define a recursive function `traverse` that takes a node as input and performs inorder traversal on the binary tree rooted at that node.
# Inside the function, we first check if the node is not None. If it is not None, we recursively call `traverse` on the left child of the current node.
# Then, we append the value of the current node to a list.
# Finally, we recursively call `traverse` on the right child of the current node.
# We initialize an empty list `l` to store the inorder traversal result and call the `traverse` function with the root of the binary tree.
# Finally, we return the list `l` containing the inorder traversal result.

# Complexity
# Time complexity: O(n), where n is the number of nodes in the binary tree. We visit each node once.
# Space complexity: O(n), where n is the number of nodes in the binary tree. This represents the space used by the list `l` to store the inorder traversal result.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []

        def traverse(root):
            if root:
                traverse(root.left)
                l.append(root.val)
                traverse(root.right)

        traverse(root)
        return l
