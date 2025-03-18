int MinJumps(IReadOnlyList<int> arr)
{
	var n = arr.Count;
	if (n <= 1)
		return 0;
	var queue = new Queue<(int, int, int)>();
	var start = (0, arr[0], 1);
	queue.Enqueue(start);
	while (queue.Count > 0)
	{
		var (pos, maxJump, jumps) = queue.Dequeue();
		if (CanReachEndOfArray(pos, maxJump, n))
		{
			return jumps;
		}
		for (var i = 1; i <= maxJump; i++)
		{
			if(pos + i < n)
				queue.Enqueue((pos + i, arr[pos + i], jumps + 1));
		}
	}
	return -1;
}

bool CanReachEndOfArray(int pos, int maxJump, int arrayLength)
{
	if (pos == arrayLength - 1)
		return true;
	return pos + maxJump >= arrayLength - 1;
}

Console.WriteLine(MinJumps(new[]{1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}));
Console.WriteLine(MinJumps(new[]{1, 4, 3, 2, 6, 7}));
Console.WriteLine(MinJumps(new[]{0, 10, 20}));
Console.WriteLine(MinJumps(new[]{0}));
Console.WriteLine(MinJumps(new int []{}));