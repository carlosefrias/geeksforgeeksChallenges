// Indexes of Subarray Sum
// Difficulty: MediumAccuracy: 16.5%Submissions: 1.9MPoints: 4Average Time: 20m
// Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.
//
// 				Note: If no such array is possible then, return [-1].
//
// Examples:
//
// Input: arr[] = [1, 2, 3, 7, 5], target = 12
// Output: [2, 4]
// Explanation: The sum of elements from 2nd to 4th position is 12.
// 				Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
// Output: [1, 5]
// Explanation: The sum of elements from 1st to 5th position is 15.
// 				Input: arr[] = [5, 3, 4], target = 2
// Output: [-1]
// Explanation: There is no subarray with sum 2.
// 				Constraints:
// 1 <= arr.size()<= 106
// 0 <= arr[i] <= 103
// 0 <= target <= 109
//
// Expected Complexities

using System.Numerics;

List<int> SubarraySum(int[] arr, int target)
{
	for (int startIdx = 0; startIdx < arr.Length; startIdx++)
	{
		for (int endInx = startIdx; endInx < arr.Length; endInx++)
		{
			var subArray = SubArray(arr, startIdx, endInx - startIdx + 1);
			var sum = subArray.Sum();
			if (sum == target)
			{
				return new List<int> { startIdx + 1, endInx + 1 };
			}
		}
	}
	return new List<int> { -1 };
}
T[] SubArray<T>(T[] data, int index, int length)
{
	T[] result = new T[length];
	Array.Copy(data, index, result, 0, length);
	return result;
}

// var results = SubarraySum(new []{1, 2, 3, 7, 5}, 12);
// var results1 = SubarraySum(new []{12, 18, 5, 11, 30, 5}, 69);



// Kadane's Algorithm
// Difficulty: MediumAccuracy: 36.28%Submissions: 1.2MPoints: 4Average Time: 20m
// You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].
//
// 				Note : A subarray is a continuous part of an array.
//
// 				Examples:
//
// Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
// Output: 11
// Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.
// 				Input: arr[] = [-2, -4]
// Output: -2
// Explanation: The subarray [-2] has the largest sum -2.
// 				Input: arr[] = [5, 4, 1, 7, 8]
// Output: 25
// Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.
// 				Constraints:
// 1 ≤ arr.size() ≤ 105
// 				-104 ≤ arr[i] ≤ 104
//
// Expected Complexities
// Time Complexity: O(n)
// Auxiliary Space: O(1)
int maxSubarraySum(int[] arr)
{
	// Kadane's algorithm: O(n) time, O(1) space
	if (arr.Length == 0)
		return 0; // or throw, depending on desired behavior

	int maxSoFar = arr[0];
	int currentMax = arr[0];

	for (int i = 1; i < arr.Length; i++)
	{
		currentMax = Math.Max(arr[i], currentMax + arr[i]);
		maxSoFar = Math.Max(maxSoFar, currentMax);
	}

	return maxSoFar;
}

// var maxSum1 = maxSubarraySum(new[] { 2, 3, -8, 7, -1, 2, 3 });
// var maxSum2 = maxSubarraySum(new[] { -2, -4 });
// var maxSum3 = maxSubarraySum(new[] { 5, 4, 1, 7, 8 });


// Sort 0s, 1s and 2s
// Difficulty: MediumAccuracy: 50.58%Submissions: 823K+Points: 4Average Time: 10m
// Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
// 				Note: You need to solve this problem without utilizing the built-in sort function.
//
// 				Examples:
//
// Input: arr[] = [0, 1, 2, 0, 1, 2]
// Output: [0, 0, 1, 1, 2, 2]
// Explanation: 0s, 1s and 2s are segregated into ascending order.
// 				Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
// Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
// Explanation: 0s, 1s and 2s are segregated into ascending order.
// 				Follow up: Could you come up with a one-pass algorithm using only constant extra space?
//
// 				Constraints:
// 				1 ≤ arr.size() ≤ 106
// 0 ≤ arr[i] ≤ 2
//
// Expected Complexities
// Time Complexity: O(n)
// Auxiliary Space: O(1)
void sort012(int[] arr)
{
	// code here
	var zeros = arr.Count(value => value == 0);
	var ones = arr.Count(value => value == 1);
	var twos = arr.Length - zeros - ones;
	var index = zeros;
	for (int i = 0; i < ones; i++) arr[index++] = 1;
	for (int i = 0; i < twos; i++) arr[index++] = 2;
}

// var arr1 = new[] { 0, 1, 2, 0, 1, 2 };
// sort012(arr1);
// var arr2 = new[] { 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1 };
// sort012(arr2);


// Majority Element
// Difficulty: MediumAccuracy: 27.82%Submissions: 781K+Points: 4Average Time: 59m
// Given an array arr[]. Find the majority element in the array. If no majority element exists, return -1.
//
// 				Note: A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.
//
// 				Examples:
//
// Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
// Output: 1
// Explanation: Since, 1 is present more than 7/2 times, so it is the majority element.
// 				Input: arr[] = [7]
// Output: 7
// Explanation: Since, 7 is single element and present more than 1/2 times, so it is the majority element.
// 				Input: arr[] = [2, 13]
// Output: -1
// Explanation: Since, no element is present more than 2/2 times, so there is no majority element.
// 				Constraints:
// 1 ≤ arr.size() ≤ 105
// 1 ≤ arr[i] ≤ 105
//
// Expected Complexities
// Time Complexity: O(n)
// Auxiliary Space: O(1)

int majorityElement(int[] arr)
{
	// code here
	var dic = new Dictionary<int, int>();
	var len = arr.Length;
	var half = len / 2.0;
	foreach (var value in arr)
	{
		if (dic.ContainsKey(value))
		{
			dic[value] += 1;
		}
		else
			dic.Add(value, 1);

		if (dic[value] > half)
			return value;
	}

	return -1;
}

// var m1 = majorityElement(new[] { 1, 1, 2, 1, 3, 5, 1 });
// var m2 = majorityElement(new[] { 7 });
// var m3 = majorityElement(new[] { 2, 13 });


// Directed Graph Cycle
// Difficulty: MediumAccuracy: 27.88%Submissions: 542K+Points: 4
// Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
// 				The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from verticex u to v.
//
// 				Examples:
//
// Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 0], [2, 3]]
//
//
//
// Output: true
// Explanation: The diagram clearly shows a cycle 0 → 1 → 2 → 0
// Input: V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
//
//
// Output: false
// Explanation: no cycle in the graph
// Constraints:
// 1 ≤ V ≤ 105
// 0 ≤ E ≤ 105
// 0 ≤ edges[i][0], edges[i][1] < V
//
// Expected Complexities
// Time Complexity: O(V + E)
// Auxiliary Space: O(V + E)


bool IsCyclic(int v, int[,] edges)
{
	// Dictionary containing all direct connections to a node
	var dic = new Dictionary<int, List<int>>();
	var n = edges.GetLength(0);
	for (int i = 0; i < n; i++)
	{
		var edge = new[] { edges[i, 0], edges[i, 1] };
		if (dic.ContainsKey(edge[0]))
		{
			dic[edge[0]].Add(edge[1]);
		}
		else
		{
			dic.Add(edge[0], new List<int> { edge[1] });
		}
	}
	// code here
	for (int i = 0; i < v; i++)
	{
		var visited = new bool[v];
		visited[i] = true;
		var hasCycle = Dfs(i, dic, visited);
		if (hasCycle)
			return true;
	}
	return false;
}

bool Dfs(int node, Dictionary<int, List<int>> dic, bool[] visited)
{
	if (!dic.ContainsKey(node))
		return false;
	var connections = dic[node];
	foreach (var directNode in connections)
	{
		if (visited[directNode])
			return true;
		visited[directNode] = true;
		if (Dfs(directNode, dic, visited))
			return true;
		visited[directNode] = false;
	}
	return false;
}

// var x = IsCyclic(4, new[,]
// {
// 	{ 0, 1 },
// 	{ 1, 2 },
// 	{ 2, 0 },
// 	{ 2, 3 }
// });
//
//
// var x1 = IsCyclic(4, new[,]
// {
// 	{ 0, 1 },
// 	{ 0, 2 },
// 	{ 1, 2 },
// 	{ 2, 3 }
// });

//
// Dijkstra Algorithm
// Difficulty: MediumAccuracy: 50.83%Submissions: 262K+Points: 4Average Time: 25m
// Given an undirected, weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by 2d array edges[][],
// where edges[i]=[u, v, w] represents the edge between the nodes u and v having w edge weight.
// 				You have to find the shortest distance of all the vertices from the source vertex src,
// and return an array of integers where the ith element denotes the shortest distance between ith node and source vertex src.
//
// 				Note: The Graph is connected and doesn't contain any negative weight edge.
// 				It is guaranteed that all the shortest distance will fit in a 32-bit integer.
//
// 				Examples:
//
// Input: V = 3, edges[][] = [[0, 1, 1], [1, 2, 3], [0, 2, 6]], src = 2
// Output: [4, 3, 0]
// Explanation:
//
// Shortest Paths:
// For 2 to 0 minimum distance will be 4. By following path 2 -> 1 -> 0
// For 2 to 1 minimum distance will be 3. By following path 2 -> 1
// For 2 to 2 minimum distance will be 0. By following path 2 -> 2
// Input: V = 5, edges[][] = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]], src = 0
// Output: [0, 4, 8, 10, 10]
// Explanation: 
//
// Shortest Paths: 
// For 0 to 1 minimum distance will be 4. By following path 0 -> 1
// For 0 to 2 minimum distance will be 8. By following path 0 -> 2
// For 0 to 3 minimum distance will be 10. By following path 0 -> 2 -> 3 
// For 0 to 4 minimum distance will be 10. By following path 0 -> 1 -> 4
// Constraints:
// 1 ≤ V ≤ 106
// 1 ≤ E = edges.size() ≤ 106
// 0 ≤ edges[i][0], edges[i][1] ≤ V-1
// 0 ≤ edges[i][2] ≤ 104
// 0 ≤ src < V
// Expected Complexities
// Time Complexity: O((V + E) log V)
// Auxiliary Space: O(V)


int[] Dijkstra(int V, int[,] edges, int src)
{
	var graph = new List<List<int[]>>();
	for (int i = 0; i < V; i++)
	{
		graph.Add(new List<int[]>());
	}

	for (int i = 0; i < edges.GetLength(0); i++)
	{
		var edge = new[] { edges[i, 0], edges[i, 1], edges[i, 2] };
		var u = edge[0];
		var v = edge[1];
		var w = edge[2];
		graph[u].Add(new[] { v, w });
		graph[v].Add(new[] { u, w });
	}

	var dist = new int[V];
	var visited = new bool[V];
	// foreach (var dt in dist)
	for (int i = 0; i < V; i++)
	{
		dist[i] = int.MaxValue;
	}

	dist[src] = 0;
	for (int count = 0; count < V - 1; count++)
	{
		int u = -1;
		for (int i = 0; i < V; i++)
		{
			if (!visited[i] && (u == -1 || dist[i] < dist[u]))
			{
				u = i;
			}
		}
		if (dist[u] == int.MaxValue)
			break;

		visited[u] = true;

		foreach (var neighbor in graph[u])
		{
			var v = neighbor[0];
			var weight = neighbor[1];
			if (!visited[v] && dist[u] != int.MaxValue && dist[u] + weight < dist[v])
				dist[v] = dist[u] + weight;
		}
	}
	return dist;
}

// var weights = Dijkstra(3, new[,] { { 0, 1, 1 }, { 1, 2, 3 }, { 0, 2, 6 } }, 2);

// Steps by Knight
// Difficulty: MediumAccuracy: 37.32%Submissions: 130K+Points: 4Average Time: 20m
// Given a square chessboard of size (n x n), the initial position and target postion of Knight are given.
// Find out the minimum steps a Knight will take to reach the target position.
//
// 				Note: The initial and the target position coordinates of Knight have been given according to 1-base indexing.
//
// 				Examples:
//
// Input: n = 3, knightPos[] = [3, 3], targetPos[]= [1, 2]
// Output: 1
// Explanation:
// Knight takes 1 step to reach from 
// (3, 3) to (1 ,2).
// 				Input: n = 6, knightPos[] = [4, 5],targetPos[] = [1, 1]
// Output: 3
// Explanation:
//
// Knight takes 3 step to reach from 
// (4, 5) to (1, 1):
// (4, 5) -> (5, 3) -> (3, 2) -> (1, 1).
// 				Constraints:
// 1 <= n<= 1000
// 1 <= knightpos ≤ [x, y], targertpos[x, y] ≤  n 
//
// 				Expected Complexities
// 				Time Complexity: O(n^2)
// Auxiliary Space: O(n^2)

int minStepToReachTarget(List<int> knightPos, List<int> targetPos, int n)
{
	// Code here
	var sr = knightPos[0] - 1;
	var sc = knightPos[1] - 1;
	var tr = targetPos[0] - 1;
	var tc = targetPos[1] - 1;
	if (sr == tr && sc == tc) return 0;
	return BfsOptimized(sr, sc, tr, tc, n);
}

int BfsOptimized(int sr, int sc, int tr, int tc, int n)
{
	// Precomputed move offsets (no allocation per node)
	int[,] offsets = {
		{ 1, 2 }, { -1, 2 }, { 1, -2 }, { -1, -2 },
		{ 2, 1 }, { -2, 1 }, { 2, -1 }, { -2, -1 }
	};

	var visited = new bool[n, n];
	var q = new Queue<(int r, int c)>();
	q.Enqueue((sr, sc));
	visited[sr, sc] = true;

	int steps = 0;
	while (q.Count > 0)
	{
		int levelCount = q.Count;
		for (int i = 0; i < levelCount; i++)
		{
			var (r, c) = q.Dequeue();
			if (r == tr && c == tc) return steps;

			for (int k = 0; k < 8; k++)
			{
				int nr = r + offsets[k, 0];
				int nc = c + offsets[k, 1];
				if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr, nc])
				{
					visited[nr, nc] = true; // mark ON enqueue to avoid duplicates
					q.Enqueue((nr, nc));
				}
			}
		}
		steps++;
	}

	return -1;
}

// var c = minStepToReachTarget(new List<int> { 3, 3 }, new List<int> { 1, 2 }, 3);
// var c1 = minStepToReachTarget(new List<int> { 4, 5 }, new List<int> { 1, 1 }, 6);


// Nth Fibonacci Number
// Difficulty: EasyAccuracy: 22.3%Submissions: 379K+Points: 2
// Given a non-negative integer n, your task is to find the nth Fibonacci number.
//
// 				The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are 0 followed by 1. The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21
//
// The Fibonacci sequence is defined as follows:
//
// F(0) = 0
// F(1) = 1
// F(n) = F(n - 1) + F(n - 2) for n > 1
// Examples :
//
// Input: n = 5
// Output: 5
// Explanation: The 5th Fibonacci number is 5.
// 				Input: n = 0
// Output: 0 
// Explanation: The 0th Fibonacci number is 0.
// 				Input: n = 1
// Output: 1
// Explanation: The 1st Fibonacci number is 1.
// 				Constraints:
// 0 ≤ n ≤ 30
//
// Expected Complexities
// Time Complexity: O(n)
// Auxiliary Space: O(1)

int nthFibonacci(int n) {
	// code here
	var memo = new Dictionary<int, int>
	{
		{ 0, 0 },
		{ 1, 1 }
	};
	if (n < 2)
		return memo[n];
	for (int i = 2; i <= n; i++)
	{
		memo.Add(i, memo[i-1] + memo[i-2]);
	}

	return memo[n];
}

// var f1 = nthFibonacci(5);
// var f2 = nthFibonacci(0);
// var f3 = nthFibonacci(1);
// var f4 = nthFibonacci(20);

// Minimum Operations
// Difficulty: EasyAccuracy: 60.02%Submissions: 105K+Points: 2
// Given a number n. Find the minimum number of operations required to reach n starting from 0. You have two operations available:
//
// Double the number
// 				Add one to the number
// Example 1:
//
// Input: n = 8
// Output: 4
// Explanation: 0 + 1 = 1 --> 1 + 1 = 2 --> 2 * 2 = 4 --> 4 * 2 = 8.
// 				Example 2:
//
// Input: n = 7
// Output: 5
// Explanation: 0 + 1 = 1 --> 1 + 1 = 2 --> 1 + 2 = 3 --> 3 * 2 = 6 --> 6 + 1 = 7.
// 				Constraints:
// 1 <= n <= 106
//
// Expected Complexities
// Time Complexity: O(log n)
// Auxiliary Space: O(1)

int minOperation(int n) {
	// Your code here
	if (n == 0)
		return 0;
	var dp = new int [n + 1];
	for (int i = 1; i <= n; i++)
	{
		if (i % 2 == 0)
			dp[i] = Math.Min(1 + dp[i - 1], 1 + dp[i / 2]);
		else
			dp[i] = 1 + dp[i - 1];
	}

	return dp[n];
}

// var minOps1 = minOperation(8); //expected output 4
// var minOps2 = minOperation(7); //expected output 5
// var minOps3 = minOperation(3); //expected output 3


// nCr
// Difficulty: MediumAccuracy: 14.82%Submissions: 353K+Points: 4
// Given two integer values n and r, the task is to find the value of Binomial Coefficient nCr
//
// A binomial coefficient nCr can be defined as the coefficient of xr in the expansion of (1 + x)n that gives the number of ways to choose r objects from a set of n objects without considering the order.
// 				The binomial coefficient nCr is calculated as : C(n,r) = n! / r! * (n-r) !
// Note: If r is greater than n, return 0.
// 				It is guaranteed that the value of nCr will fit within a 32-bit integer.
//
// 				Examples:
//
// Input: n = 5, r = 2
// Output: 10
// Explaination: The value of 5C2 is calculated as 5!/(5−2)!*2! = 5!/3!*2! = 10.
// 				Input: n = 2, r = 4
// Output: 0
// Explaination: Since r is greater than n, thus 2C4 = 0
// Input: n = 5, r = 0
// Output: 1
// Explaination: The value of 5C0 is calculated as 5!/(5−0)!*0! = 5!/5!*0! = 1.
// 				Constraints:
// 1 ≤ n ≤ 100
// 0 ≤ r ≤ 100
//
// Expected Complexities
// Time Complexity: O(n)
// Auxiliary Space: O(1)

Dictionary<int, ulong> FactorialCache = new Dictionary<int, ulong>
{
	{0,1},
	{1,1}
};

int nCr(int n, int r)
{
	if (r > n)
		return 0;
	var res = Factorial(n) / (Factorial(n - r) * Factorial(r));
	return (int)res;
}

ulong Factorial(int n)
{
	if (FactorialCache.ContainsKey(n))
		return FactorialCache[n];
	FactorialCache.Add(n, (ulong)n * Factorial(n - 1));
	return FactorialCache[n];
}

// var c52 = nCr(5, 2);
// var c24 = nCr(2, 4);
// var c50 = nCr(5, 0);
// var c21_16 = nCr(21, 16);


// Longest Palindrome in a String
// Difficulty: MediumAccuracy: 23.2%Submissions: 342K+Points: 4
// Given a string s, your task is to find the longest palindromic substring within s.
//
// 				A substring is a contiguous sequence of characters within a string, defined as s[i...j] where 0 ≤ i ≤ j < len(s).
//
// 				A palindrome is a string that reads the same forward and backward. More formally, s is a palindrome if reverse(s) == s.
//
// 				Note: If there are multiple palindromic substrings with the same length, return the first occurrence of the longest palindromic substring from left to right.
//
// 				Examples :
//
// Input: s = “forgeeksskeegfor” 
// Output: “geeksskeeg”
// Explanation: There are several possible palindromic substrings like “kssk”, “ss”, “eeksskee” etc. But the substring “geeksskeeg” is the longest among all.
// 				Input: s = “Geeks” 
// Output: “ee”
// Explanation: "ee" is the longest palindromic substring of "Geeks". 
// 				Input: s = “abc” 
// Output: “a”
// Explanation: "a", "b" and "c" are longest palindromic substrings of same length. So, the first occurrence is returned.
// 				Constraints:
// 1 ≤ s.size() ≤ 103
// s consist of only lowercase English letters.
//
// 				Expected Complexities
// Time Complexity: O(n^2)
// Auxiliary Space: O(1)

string longestPalindrome(string s) {
	if (string.IsNullOrEmpty(s))
		return s;
	var len = s.Length;
	bool[,] dp = new bool[len, len];

	for (int i = 0; i < len; i++)
	{
		dp[i, i] = true;
	}

	var longestStart = 0;
	var longestLength = 1;

	for (int i = 0; i < len - 1; i++)
	{
		var isPal = s[i] == s[i + 1];
		dp[i, i + 1] = isPal;
		if (isPal && longestLength == 1)
		{
			longestStart = i;
			longestLength = 2;
		}
	}

	for (int size = 3; size <= len; size++)
	{
		for (int i = 0; i <= len - size; i++)
		{
			var j = i + size - 1;
			var isPal = s[i] == s[j] && dp[i + 1, j - 1];
			if (isPal)
			{
				dp[i, j] = true;
				if (size > longestLength)
				{
					longestStart = i;
					longestLength = size;
				}
			}
		}
	}

	return s.Substring(longestStart, longestLength);
}

// var pal1 = longestPalindrome("forgeeksskeegfor");
// var pal2 = longestPalindrome("Geeks");
// var pal3 = longestPalindrome("aabbaa");

// Maximize The Cut Segments
// Difficulty: MediumAccuracy: 24.29%Submissions: 257K+Points: 4
// Given an integer n denoting the Length of a line segment. You need to cut the line segment in such a way that the cut length
// of a line segment each time is either x , y or z. Here x, y, and z are integers.
// 				After performing all the cut operations, your total number of cut segments must be maximum.
// Return the maximum number of cut segments possible.
//
// 				Note: if no segment can be cut then return 0.
//
// 				Examples:
//
// Input: n = 4, x = 2, y = 1, z = 1
// Output: 4
// Explanation: Total length is 4, and the cut lengths are 2, 1 and 1.  We can make maximum 4 segments each of length 1.
// 				Input: n = 5, x = 5, y = 3, z = 2
// Output: 2
// Explanation: Here total length is 5, and the cut lengths are 5, 3 and 2. We can make two segments of lengths 3 and 2.
// 				Input: n = 7, x = 8, y = 9, z = 10
// Output: 0
// Explanation: Here the total length is 7, and the cut lengths are 8, 9, and 10. We cannot cut the segment into lengths that fully utilize the segment, so the output is 0.
// 				Constraints
// 1 <= n, x, y, z <= 104
//
// Expected Complexities
// Time Complexity: O(n)
// Auxiliary Space: O(n)

int maximizeTheCuts(int n, int x, int y, int z) {
	var dp = new int[n + 1];
	for (int i = 0; i < n +1; i++)
	{
		dp[i] = -1; //filling the initial values
	}
	dp[0] = 0; //If length 0 we can't cut it
	for (int i = 1; i <= n; i++)
	{
		if (i >= x && dp[i - x] != -1)
			dp[i] = Math.Max(dp[i], dp[i - x] + 1);
		if (i >= y && dp[i - y] != -1) 
			dp[i] = Math.Max(dp[i], dp[i - y] + 1);
		if (i >= z && dp[i - z] != -1)
			dp[i] = Math.Max(dp[i], dp[i - z] + 1);
	}
	return dp[n] == -1 ? 0 : dp[n];
}

// var mc1 = maximizeTheCuts(4, 2, 1, 1);
// var mc3 = maximizeTheCuts(5, 5, 3, 2);
// var mc2 = maximizeTheCuts(7, 8, 9, 10);

// Longest Subarray with Sum K
// Difficulty: MediumAccuracy: 24.64%Submissions: 750K+Points: 4
// Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.
//
// 				Examples:
//
// Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
// Output: 6
// Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.
// 				Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
// Output: 5
// Explanation: Only subarray with sum = -5 is [-5, 8, -14, 2, 4] of length 5.
// 				Input: arr[] = [10, -10, 20, 30], k = 5
// Output: 0
// Explanation: No subarray with sum = 5 is present in arr[].
// 				Constraints:
// 1 ≤ arr.size() ≤ 105
// 				-104 ≤ arr[i] ≤ 104
// 				-109 ≤ k ≤ 109
//
// Expected Complexities
// Time Complexity: O(n)
// Auxiliary Space: O(n)

int longestSubarrayMine(int[] arr, int k) {
	// code here
	int lenght = arr.Length;
	while (lenght > 0)
	{
		for (int idx = 0; idx <= arr.Length - lenght; idx++)
		{
			var subArray = GetSubArray(arr, idx, lenght);
			if (subArray.Sum() == k)
				return lenght;
		}
		lenght--;
	}
	return lenght;
}

int longestSubarray(int[] arr, int k) {
	// O(n) prefix-sum + hashmap; supports negative values
	var firstIndex = new Dictionary<long, int>();
	long sum = 0;
	int maxLen = 0;
	firstIndex[0] = -1; // prefix sum 0 at index -1

	for (int i = 0; i < arr.Length; i++)
	{
		sum += arr[i];
		// record earliest occurrence of this prefix sum
		if (!firstIndex.ContainsKey(sum))
			firstIndex[sum] = i;

		long need = sum - k;
		if (firstIndex.TryGetValue(need, out int startIdx))
		{
			int len = i - startIdx;
			if (len > maxLen) maxLen = len;
		}
	}
	return maxLen;
}

int[] GetSubArray(int[] arr, int idx, int length)
{
	var res = new int [length];
	var c = 0;
	for (int i = idx; i < idx + length; i++)
	{
		res[c++] = arr[i];
	}
	return res;
}

// var ls1 = longestSubarray(new[] { 10, 5, 2, 7, 1, -10 }, 15);
// var ls2 = longestSubarray(new[] { -5, 8, -14, 2, 4, 12 }, -5);
// var ls3 = longestSubarray(new[] { 10, -10, 20, 30 }, 5);
// var ls4 = longestSubarray(new[] { 94, -33, -13, 40, -82, 94, -33, -13, 40, -82 }, 52);


// Kth Smallest
// Difficulty: MediumAccuracy: 35.17%Submissions: 726K+Points: 4Average Time: 25m
// Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.
//
// 				Examples :
//
// Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
// Output: 5
// Explanation: 4th smallest element in the given array is 5.
// 				Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
// Output: 7
// Explanation: 3rd smallest element in the given array is 7.
// 				Constraints:
// 1 ≤ arr.size() ≤ 105
// 1 ≤ arr[i] ≤ 105
// 1 ≤ k ≤  arr.size() 
//
// Expected Complexities
// Time Complexity: O(n log k)
// Auxiliary Space: O(k)

int kthSmallest(int[] arr, int k) {
	// Code Here
	return arr.OrderBy(val => val).Take(k).Last();
}

// var ks = kthSmallest(new[] { 10, 5, 4, 3, 48, 6, 2, 33, 53, 10 }, 4);
// var ks1 = kthSmallest(new[] { 7, 10, 4, 3, 20, 15 }, 3);

// Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.
//
// 				Return true if such a triplet exists, otherwise, return false.
//
// 				Examples: 
//
// Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
// Output: true 
// Explanation: The triplet {1, 4, 8} sums up to 13.
// 				Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10
// Output: true 
// Explanation: The triplets {1, 3, 6} and {1, 2, 7} both sum to 10. 
// 				Input: arr[] = [40, 20, 10, 3, 6, 7], target = 24
// Output: false 
// Explanation: No triplet in the array sums to 24.
// 				Constraints:
// 3 ≤ arr.size() ≤ 5*103
// 0 ≤ arr[i], target ≤ 105
//
// Expected Complexities
// Time Complexity: O(n^2)
// Auxiliary Space: O(1)

bool hasTripletSum(int[] arr, int target) {
	var sum = arr.Sum();
	if (sum < target)
		return false;
	//sort arr
	var sorted = arr.OrderBy(val => val).ToArray();
	for (int i = 0; i < arr.Length; i++)
	{
		var ptrStart = i + 1;
		var ptrEnd = arr.Length - 1;
		var firstElement = sorted[i];
		var remaining = target - firstElement;
		while (ptrEnd > ptrStart)
		{
			var currentSum = sorted[ptrStart] + sorted[ptrEnd];
			if (currentSum == remaining)
				return true;
			if (currentSum > remaining)
				ptrEnd--;
			if (currentSum < remaining)
				ptrStart++;
		}
	}
	return false;
}

var trip1 = hasTripletSum(new[] { 1, 4, 45, 6, 10, 8 }, 13);
var trip2 = hasTripletSum(new[] { 1, 2, 4, 3, 6, 7 }, 10);
var trip3 = hasTripletSum(new[] { 40, 20, 10, 3, 6, 7 }, 24);
Console.WriteLine("end");