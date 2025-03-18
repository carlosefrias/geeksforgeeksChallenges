bool IsSubsetSum(int[] arr, int sum)
{
	arr = arr.Where(val => val <= sum).ToArray();
	var queue = new Queue<List<int>>();
	var start = new List<int>();
	queue.Enqueue(start);
	while (queue.Count > 0)
	{
		var current = queue.Dequeue();
		var currentSum = current.Sum();
		if (currentSum == sum)
		{
			Console.WriteLine($"{string.Join("+", current)}={sum}");
			return true;	
		}
		foreach (var value in arr)
		{
			if (current.Contains(value)) continue;
			if (currentSum + value > sum) continue;
			var next = current.ToList();
			next.Add(value);
			queue.Enqueue(next);
		}
	}
	return false;
}

Console.WriteLine(IsSubsetSum(new []{3, 34, 4, 12, 5, 2}, 9));
Console.WriteLine(IsSubsetSum(new []{3, 34, 4, 12, 5, 2}, 30));
Console.WriteLine(IsSubsetSum(new []{1, 2, 3}, 6));