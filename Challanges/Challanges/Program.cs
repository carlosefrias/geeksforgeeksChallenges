// See https://aka.ms/new-console-template for more information

// Max Sum Increasing Subsequence
// Difficulty: MediumAccuracy: 40.02%Submissions: 220K+Points: 4Average Time: 25m
// Given an array of positive integers arr[], find the maximum sum of a subsequence such that the elements of the subsequence form a strictly increasing sequence.
// 				In other words, among all strictly increasing subsequences of the array, return the one with the largest possible sum.
//
// 				Examples:
//
// Input: arr[] = [1, 101, 2, 3, 100]
// Output: 106
// Explanation: The maximum sum of an increasing sequence is obtained from [1, 2, 3, 100].
// Input: arr[] = [4, 1, 2, 3]
// Output: 6
// Explanation: The maximum sum of an increasing sequence is obtained from [1, 2, 3].
// Input: arr[] = [4, 1, 2, 4]
// Output: 7
// Explanation: The maximum sum of an increasing sequence is obtained from [1, 2, 4].
// Constraints:
// 1 ≤ arr.size() ≤ 103
// 1 ≤ arr[i] ≤ 105
//
// Expected Complexities
// Time Complexity: O(n log n)
// Auxiliary Space: O(n)

int MaxSumIs(IReadOnlyList<int> array)
{
	var n = array.Count;
	var dp = new int[n];
	Console.WriteLine(string.Join(',', dp));
	for (var i = 0; i < n; i++)
	{
		dp[i] = array[i];
		for (var j = 0; j < i; j++)
		{
			if (array[j] < array[i])
			{
				dp[i] = Math.Max(dp[i], dp[j] + array[i]);
			}
			Console.WriteLine(string.Join(',', dp));
		}
	}
	return dp.Max();
}

// Console.WriteLine(MaxSumIs(new []{1, 101, 2, 3, 100 }));


// # Longest Common Increasing Subsequence
// # Difficulty: MediumAccuracy: 40.62%Submissions: 21K+Points: 4
// # Given two arrays, a[] and b[], find the length of the longest common increasing subsequence(LCIS).
//
// # Note:  LCIS refers to a subsequence that is present in both arrays and strictly increases.
//
// # Examples:
//
// # Input: a[] = [3, 4, 9, 1], b[] = [5, 3, 8, 9, 10, 2, 1]
// # Output: 2
// # Explanation: The longest increasing subsequence that is common is [3, 9] and its length is 2.
// # Input: a[] = [1, 1, 4, 3], b[] = [1, 1, 3, 4]
// # Output: 2
// # Explanation: There are two common subsequences [1, 4] and [1, 3] both of length 2.
// # Constraints:
// # 1 ≤ a.size(), b.size() ≤ 103
// # 1 ≤ a[i], b[i] ≤ 104
//
// # Expected Complexities
// # Time Complexity: O(n * m)
// # Auxiliary Space: O(n)

int Lcis(int[] a, int[] b)
{
	var n = a.Length;
	var m = b.Length;
	var dp = new int[m];
	for (int i = 0; i < n; i++)
	{
		var current = 0;
		for (int j = 0; j < m; j++)
		{
			if (a[i] == b[j])
			{
				dp[j] = Math.Max(dp[j], current + 1);
			}
			else if (a[i] > b[j])
			{
				current = Math.Max(current, dp[j]);
			}
		}	
	}

	return dp.Max();
}

Console.WriteLine(Lcis(new[]{3, 4, 9, 1}, new []{5, 3, 8, 9, 10, 2, 1}));
Console.WriteLine(Lcis(new[]{1, 1, 4, 3}, new []{1, 1, 3, 4}));

