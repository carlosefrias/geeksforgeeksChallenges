# Maximum Non-Adjacent Nodes Sum
# Difficulty: MediumAccuracy: 55.35%Submissions: 97K+Points: 4Average Time: 45m
# Given the root of a binary tree with integer values. Your task is to select a subset of nodes such that the sum of their values is maximized, with the condition that no two selected nodes are directly connected that is, if a node is included in the subset, neither its parent nor its children can be included.

# Examples:

# Input: root = [11, 1, 2]

# Output: 11
# Explanation: The maximum sum is obtained by selecting the node 11.

# Input: root = [1, 2, 3, 4, N, 5, 6]

# Output: 16
# Explanation: The maximum sum is obtained by selecting the nodes 1, 4, 5 and 6, which are not directly connected to each other. Their total sum is 16.  

# Constraints:
# 1 ≤ number of nodes ≤ 104
# 1 ≤ node.data ≤ 105
# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(n)


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def getMaxSum(self, root):
        def solve(node):
            if not node:
                return (0, 0)  # (include, exclude)
            
            # Recursively solve for left and right subtrees
            left = solve(node.left)
            right = solve(node.right)
            
            # If we include current node, we cannot include its children
            include = node.data + left[1] + right[1]
            
            # If we exclude current node, we can choose to include or exclude children
            # We take the maximum of including or excluding each child
            exclude = max(left[0], left[1]) + max(right[0], right[1])
            return (include, exclude)
        
        result = solve(root)
        return max(result[0], result[1])

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
        # ([11, 1, 2], 11),
        ([1, 2, 3, 4, None, 5, 6], 16)
    ]
    for i, (input_list, expected) in enumerate(test_cases, 1):
        root = build_tree_from_list(input_list)
        result = sol.getMaxSum(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status} - Expected: {expected}, Got: {result}")

test_with_level_order()
