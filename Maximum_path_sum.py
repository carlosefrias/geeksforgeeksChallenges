# Maximum path sum
# Difficulty: MediumAccuracy: 42.92%Submissions: 113K+Points: 4Average Time: 45m
# Given the root of a binary tree, your task is to find the maximum path sum. The path may start and end at any node in the tree.

# Examples:

# Input: root[] = [10, 2, 10, 20, 1, N, -25, N, N, N, N, 3, 4]
# Output: 42
# Explanation: Max path sum is represented using green colour nodes in the above binary tree.

# Input: root[] = [-17, 11, 4, 20, -2, 10]
# Output: 31
# Explanation: Max path sum is represented using green colour nodes in the above binary tree.

# Constraints:
# 1 ≤ number of nodes ≤ 103
# -104 ≤ node->data ≤ 104

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(h)


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def findMaxSum(self, root): 
        # use DFS that returns max downward path sum and update global max for any path
        max_sum = float('-inf')
        def dfs(node):
            nonlocal max_sum
            if node is None:
                return 0
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            # price of the new path that passes through this node
            current_path = node.data + left_gain + right_gain
            if current_path > max_sum:
                max_sum = current_path
            # return max gain to parent (can't take both children)
            return node.data + max(left_gain, right_gain)
        dfs(root)
        return max_sum


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
        ([10, 2, 10, 20, 1, None, -25, None, None, None, None, 3, 4], 42),
        ([-17, 11, 4, 20, -2, 10], 31)
    ]
    for i, (input_list, expected) in enumerate(test_cases, 1):
        root = build_tree_from_list(input_list)
        result = sol.findMaxSum(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status} - Expected: {expected}, Got: {result}")

test_with_level_order()