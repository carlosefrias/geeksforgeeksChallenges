int Bfs(int[] coins, int target)
{
	if (target == 0)
		return 0;
	if (target < coins.Min())
		return 0;
	var ways = new HashSet<string>();
	var queue = new Queue<List<int>>();
	var start = new List<int> ();
	queue.Enqueue(start);
	while (queue.Count > 0)
	{
		var current = queue.Dequeue();
		if (current.Sum() == target)
		{
			current.Sort();
			var str = $"[{string.Join(',', current)}]";
			if (!ways.Contains(str))
			{
				Console.WriteLine(str);
				ways.Add(str);
			}	
		}
		foreach (var coin in coins)
		{
			var next = current.ToList();
			next.Add(coin);
			if(next.Sum() <= target)
				queue.Enqueue(next);
		}
	}
	return ways.Count;
}

int CountCoinChange(int[] coins, int target)
{
	return Bfs(coins, target);
}
Console.WriteLine(CountCoinChange(new []{1, 2, 3}, 4));
Console.WriteLine(CountCoinChange(new []{2, 5, 3, 6}, 10));
Console.WriteLine(CountCoinChange(new []{5, 10}, 3));