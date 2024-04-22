# Intuition
# One way to solve this problem is to traverse the binary tree recursively and keep track of the current path from the root to the current node.
# When we reach a leaf node, we add the current path to the list of all paths.

# Approach
# We define a recursive function `findPaths` that takes a node, the current path, and a list to store all paths as input.
# Inside the function, we append the value of the current node to the current path.
# If the current node is a leaf node, we append the current path to the list of all paths.
# Otherwise, we recursively call `findPaths` on the left and right children of the current node.
# We initialize an empty list to store all paths and call `findPaths` with the root node and an empty string as the initial path.
# Finally, we return the list of all paths.

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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def findPaths(root, path, allpath):
            if root is None:
                return
            if path == "":
                path = path + str(root.val)
            else:
                path = path + "->" + str(root.val)
            if root.left is None and root.right is None:
                allpath.append(path)
                return
            findPaths(root.left, path, allpath)
            findPaths(root.right, path, allpath)

        all_paths = []
        findPaths(root, "", all_paths)
        return all_paths
