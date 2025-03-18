bool EqualPartition(IReadOnlyList<int> arr)
{
	var len = arr.Count;
	if (arr.Count == 0)
		return false;
	var sum = arr.Sum();
	if (sum % 2 == 1)
		return false;
	var half = sum / 2;
	var queue = new Queue<(List<int>,int)>();
	var start = (new List<int>{0}, arr[0]);
	queue.Enqueue(start);
	while (queue.Count > 0)
	{
		var current = queue.Dequeue();
		var currentSum = current.Item2;
		if(currentSum > half)
			continue;
		if(current.Item1.Count == len)
			continue;
		if (currentSum == half)
		{
			var complementaryGroup = new List<int>();
			for (var i = 0; i < arr.Count; i++) { if(!current.Item1.Contains(i)) complementaryGroup.Add(i);}
			Console.WriteLine($"partition 1: [{string.Join(",", current.Item1.Select(i => arr[i]))}]");
			Console.WriteLine($"partition 2: [{string.Join(",", complementaryGroup.Select(i => arr[i]))}]");
			return true;
		}

		for (var i = 0; i < arr.Count; i++)
		{
			if (current.Item1.Contains(i)) continue;
			var next = current.Item1.ToList();
			next.Add(i);
			var nextSum = current.Item2 + arr[i];
			queue.Enqueue((next, nextSum));
		}
	}
	return false;
}
Console.WriteLine(EqualPartition(new []{1, 5, 11, 5}));
Console.WriteLine(EqualPartition(new []{1, 3, 5}));
Console.WriteLine(EqualPartition(new []{1,1,1,2,3}));