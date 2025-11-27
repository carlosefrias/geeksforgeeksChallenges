#You are given the root of a binary tree with n nodes, where each node contains a certain number of candies, and the total number of candies across all nodes is n. In one move, you can select any two adjacent nodes and transfer one candy from one node to the other. The transfer can occur between a parent and child in either direction.

#The task is to determine the minimum number of moves required to ensure that every node in the tree has exactly one candy.

#Note: The testcases are framed such that it is always possible to achieve a configuration in which every node has exactly one candy, after some moves.

#Examples:

#Input: root = [5, 0, 0, N, N, 0, 0]
  
#Output: 6
#Explanation:
#Move 1 candy from root to left child
#Move 1 candy from root to right child
#Move 1 candy from right child to root->right->left node
#Move 1 candy from root to right child
#Move 1 candy from right child to root->right->right node
#Move 1 candy from root to right child
#so, total 6 moves required.
#Input: root = [2, 0, 0, N, N, 3, 0]
  
#Output: 4
#Explanation:
#Move 1 candy from root to left child
#Move 1 candy from root->right->left node to root->right node
#Move 1 candy from root->right node to root->right->right node
#Move 1 candy from root->right->left node to root->right node
#so, total 4 moves required.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def _build_tree_from_list(arr):
    if not arr:
        return None
    # create node objects or None placeholders
    nodes = [None if v is None else TreeNode(v) for v in arr]
    root = nodes[0]
    q = [root]
    i = 1
    for node in q:
        if node is None:
            continue
        if i < len(nodes):
            node.left = nodes[i]
            i += 1
            q.append(node.left)
        if i < len(nodes):
            node.right = nodes[i]
            i += 1
            q.append(node.right)
    return root

def distCandy(root):
    # Accept level-order list input or TreeNode root
    if root is None:
        return 0
    if isinstance(root, (list, tuple)):
        root = _build_tree_from_list(list(root))

    moves = 0

    def dfs(node):
        nonlocal moves
        if node is None:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        moves += abs(left) + abs(right)
        return node.val + left + right - 1

    dfs(root)
    return moves

if __name__ == "__main__":
    # quick example
    print(distCandy([5, 0, 0, None, None, 0, 0]))  # expected 6
