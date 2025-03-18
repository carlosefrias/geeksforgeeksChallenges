int Dsf(int x, int y, ISet<(int, int)> visited, IReadOnlyList<int[]> grid)
{
	var m = grid.Count;
	var n = grid[0].Length;
	var node = (x, y);
	if (visited.Contains(node))
		return 0;
	if (grid[x][y] == 0)
		return 0;
	
	visited.Add((x,y));
	Console.WriteLine($"[{string.Join(',', visited.Select(item => $"{grid[item.Item1][item.Item2]}"))}]");
	var gold = (from xNextNode in new[] { x + 1, x, x - 1}.Where(val => val >= 0 && val < m)
					from yNextNode in new [] { y + 1, y, y - 1}.Where(val => val >= 0 && val < n)
					where xNextNode == x || yNextNode == y
					where grid[xNextNode][yNextNode] > 0
					select grid[x][y] + Dsf(xNextNode, yNextNode, visited, grid)
					).Prepend(0)
					.Max();
	visited.Remove(node);
	return gold;
}
int GetMaximumGold(IReadOnlyList<int[]> grid)
{
	var m = grid.Count;
	var n = grid[0].Length;
	var nonZeroPositions = new List<(int, int)>();
	for (var x = 0; x < m; x++)
		for (var y = 0; y < n; y++)
			if(grid[x][y] > 0)
				nonZeroPositions.Add((x,y));
	return nonZeroPositions.Max(pos => Dsf(pos.Item1, pos.Item2, new HashSet<(int, int)>(), grid));
}
Console.WriteLine(GetMaximumGold(new[] { new[] { 0, 6, 0 }, new[] { 5, 8, 7 }, new[] { 0, 9, 0 } }));

/*

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
 */