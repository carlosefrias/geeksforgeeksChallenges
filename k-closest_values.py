# Given the root of a Binary Search Tree, a target value, and an integer k. Your task is to find the k values in the BST that are closest to the target.

# The closest value is taken by choosing the one that gives minimum absolute difference from target.

# Note: In case two values have same absolute difference from target, choose the smaller one. The target may or may not be present in BST.
# You can return the values in any order the driver code will print them in sorted order only.

# Examples:

# Input: root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], target = 17, k = 3
     
# Output: [14, 20, 12]
# Explanation: Absolute difference of 17 wrt 14 and 20 is 3 and 3, but we choose the smaller value in case of same absolute difference. So, 14 coes first and then 20. Then, 12 and 22 have same absolute difference, i.e., 5 from 17. But we choose the smaller value, i.e., 12.
     
# Input: root = [5, 4, 8, 1], target = 5, k = 2
     
# Output: [5, 4]
# Explanation: The absolute difference of 5 wrt 5 is 0, and for 4, the absolute difference is 1.
    
# Constraints:
# 1 ≤ number of nodes, k ≤ 104
# 1 ≤ node->data, target ≤ 104

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(n)

import math

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def getKClosest(self, root, target, k):
        # code here
        values = []
        differences = []
        def inorder_traversal(node, values, differences):
            if node is None:
                return values, differences
            values, differences = inorder_traversal(node.left, values, differences)
            values.append(node.data)
            differences.append(abs(node.data - target))
            values, differences = inorder_traversal(node.right, values, differences)
            return values, differences
            
        inorder_traversal(root, values, differences)
        n = len(values)
        min = float('inf')
        min_idx = 0
        for i in range(n):
            val = differences[i]
            if val < min:
                min = val
                min_idx = i

        # implementing a sliding window to grab the k values
        result = [values[min_idx]]
        i = min_idx - 1
        j = min_idx + 1

        while len(result) < k:
            if i >= 0 and i < n and j >= 0 and j < n:
                val_i = differences[i]
                val_j = differences[j]
                if val_i <= val_j:
                    result.append(values[i])
                    i -= 1
                else:
                    result.append(values[j])
                    j += 1
            elif i < 0 and j < n:
                result.append(values[j])
                j += 1
            elif j >= n and i >= 0:
                result.append(values[i])
                i -= 1
            elif i < 0 and j >= n:
                break
            else:
                break
        return result
        
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


def tree_to_list(root):
    """Convert binary tree to level order list (like in examples)"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node:
            result.append(node.data)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values to clean up the list
    while result and result[-1] is None:
        result.pop()
    
    return result


def test_with_level_order():
    sol = Solution()
    
    # Test cases from the problem
    test_cases = [
        ([20, 8, 22, 4, 12, None, None, None, None, 10, 14], 17, 3, [14, 20, 12]),
        ([5, 4, 8, 1], 5, 2, [5, 4]),
        ([2, 1, 5, None, None, 3, 6, None, None, None, 7, None, None], 8, 3, [5, 6, 7])
    ]
    for i, (input_list, target, k, expected) in enumerate(test_cases, 1):
        root = build_tree_from_list(input_list)
        result = sol.getKClosest(root, target, k)
        status = "PASS" if result.sort() == expected.sort() else "FAIL"
        print(f"Test {i}: {status} - Expected: {expected}, Got: {result}")

test_with_level_order()


