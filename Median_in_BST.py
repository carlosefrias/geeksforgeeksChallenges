# You are given the root of a Binary Search Tree, find the median of it. 

# Let the nodes of the BST, when written in ascending order (inorder traversal), be represented as V1, V2, V3, …, Vn, where n is the total number of nodes in the BST.

# If number of nodes are even: return V(n/2)
# If number of nodes are odd: return V((n+1)/2)
# Examples:

# Input: root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14]
# 2
# Output: 12
# Explanation: The inorder of given BST is 4, 8, 10, 12, 14, 20, 22. Here, n = 7, so, here median will be ((7+1)/2)th value, i.e., 4th value, i.e, 12.
# Input: root = [5, 4, 8, 1]
# 1 
# Output: 4
# Explanation: The inorder of given BST is 1, 4, 5, 8. Here, n = 4(even), so, here median will be (4/2)th value, i.e., 2nd value, i.e, 4.
# Constraints:
# 1 ≤ number of nodes ≤ 105
# 1 ≤ node.data ≤  105

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(1)


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findMedian(self, root):
        # code here
        values = []
        def inorder_traversal(node, values):
            if node is None:
                return values
            values = inorder_traversal(node.left, values)
            values.append(node.data)
            values = inorder_traversal(node.right, values)
            return values
            
        inorder_traversal(root, values)
        n = len(values)
        if n % 2 == 0:
            return values[int(n/2) - 1]
        return values[int((1+n)/2) - 1]
            
        
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
        ([20, 8, 22, 4, 12, None, None, None, None, 10, 14], 12),
        ([5, 4, 8, 1], 4),
    ]
    for i, (input_list, expected) in enumerate(test_cases, 1):
        root = build_tree_from_list(input_list)
        result = sol.findMedian(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status} - Expected: {expected}, Got: {result}")

test_with_level_order()