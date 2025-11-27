# You are given the root of a binary tree, and your task is to return its bottom view. The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom.

# Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the latter one in the level order traversal is considered.

# Examples :

# Input: root = [1, 2, 3, 4, 5, N, 6]
    
# Output: [4, 2, 5, 3, 6]
# Explanation: The Green nodes represent the bottom view of below binary tree.
    
# Input: root = [20, 8, 22, 5, 3, 4, 25, N, N, 10, 14, N, N, 28, N]
    
# Output: [5, 10, 4, 28, 25]
# Explanation: The Green nodes represent the bottom view of below binary tree.
    
# Constraints:
# 1 ≤ number of nodes ≤ 105
# 1 ≤ node->data ≤ 105

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(n)


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def bottomView(self, root):
        # Use level-order traversal (BFS) tracking horizontal distance (hd) from root.
        # For each hd, the last node encountered in level order is the bottom-most node.
        if root is None:
            return []

        from collections import deque
        q = deque()
        q.append((root, 0))  # (node, horizontal_distance)

        hd_map = {}  # maps hd -> node.data (last seen at that hd)
        min_hd = max_hd = 0

        while q:
            node, hd = q.popleft()
            # Overwrite previous entry at this hd — level order ensures bottom-most (or latter) wins
            hd_map[hd] = node.data
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))

            if hd < min_hd:
                min_hd = hd
            if hd > max_hd:
                max_hd = hd

        # Collect results from leftmost hd to rightmost hd
        return [hd_map[i] for i in range(min_hd, max_hd + 1)]


from collections import deque

def build_tree_from_list(values):
    """Build tree from level order list (like in examples)"""
    if not values:
        return None
    
    root = Node(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
    
    return root

def test_with_level_order():
    sol = Solution()
    
    # Test cases from the problem
    test_cases = [
        ([1, 2, 3, 4, 5, None, 6], [4, 2, 5, 3, 6]),
        ([20, 8, 22, 5, 3, 4, 25, None, None, 10, 14, None, None, 28, None], [5, 10, 4, 28, 25]),
    ]
    for i, (input_list, expected) in enumerate(test_cases, 1):
        root = build_tree_from_list(input_list)
        result = sol.bottomView(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status} - Expected: {expected}, Got: {result}")

test_with_level_order()