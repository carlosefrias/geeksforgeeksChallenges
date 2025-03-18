int Bfs((int, int) start, (int, int) target, int n)
{
	var directions = new List<(int, int)> {
		(2, 1), (2, -1), (-2, 1), (-2, -1),
		(1, 2), (1, -2), (-1, 2), (-1, -2)
	};
	var queue = new Queue<((int, int) pos, int moves)>();
	var visited = new HashSet<(int, int)>();
	queue.Enqueue((start, 0));
	visited.Add(start);
	while (queue.Count > 0)
	{
		var (current, moves) = queue.Dequeue();
		if (current == target)
			return moves;
		foreach (var next in directions.Select(direction => (current.Item1 + direction.Item1, current.Item2 + direction.Item2))
						         .Where(next => next.Item1 >= 0 && next.Item1 < n && next.Item2 >= 0 && next.Item2 < n && !visited.Contains(next)))
		{
			queue.Enqueue((next, moves + 1));
			visited.Add(next);
		}
	}
	
	return -1; // Target not reachable
}
int CountMinNumberOfMoves((int, int) pos, (int, int) target, int size)
{
	return Bfs(pos, target, size);
}
// Console.WriteLine($"Minimum number of moves: {CountMinNumberOfMoves((1,3), (5,0), 6)}");
Console.WriteLine($"Minimum number of moves: {CountMinNumberOfMoves((0,0), (29,29), 30)}");

// Given a square chessboard of NxN size, the position of the Knight and the position of a target are give.
// We need to find out the minimum steps a Knight will take to reach the target position.
//Example:
// position (1,3), target position (5,0)
//output: 3 (1,3)->(3,4)->(4,2)->(5,0)

// int N = 30;
// int[] knightPos = { 1, 1 };
// int[] targetPos = { 30, 30 };