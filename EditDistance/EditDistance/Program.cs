using System.Diagnostics;

int EditDistance(string s1, string s2)
{
	var lettersToAdd = s2.Select(letter => letter).Distinct();
	var queue = new Queue<(string currentStr, List<string> changes)>();
	var start = s1;
	Console.WriteLine(s1);
	queue.Enqueue((start, new List<string>()));
	while (queue.Count > 0)
	{
		var (currentStr, changes) = queue.Dequeue();
		if (AreEqual(currentStr, s2))
		//if(currentStr == s2)
		{
			changes.ForEach(Console.WriteLine);
			return changes.Count;	
		}
		if (changes.Count >= new [] { s1.Length, s2.Length }.Max())
			continue;
		var allOneLetterRemoved = Enumerable.Range(0, currentStr.Length)
						.Select(index => currentStr.Remove(index, 1))
						.ToList();
		var allOneLetterReplaced = Enumerable.Range(0, currentStr.Length)
						.SelectMany(index =>
						{
							var str = currentStr.Remove(index, 1);
							return lettersToAdd.Select(l => str.Insert(index, "" + l));
						}).ToList();
		var allPossibleChanges = new List<string>();
		allPossibleChanges.AddRange(allOneLetterRemoved);
		allPossibleChanges.AddRange(allOneLetterReplaced);
		
		if(currentStr.Length < s2.Length)//Only consider add letter if it does not create a bigger word than s2
			allPossibleChanges.AddRange(Enumerable.Range(0, currentStr.Length + 1)
							.SelectMany(index =>
							{
								return lettersToAdd.Select(l => currentStr.Insert(index, "" + l));
							}).ToList());
		allPossibleChanges = allPossibleChanges
						.Distinct()
						.ToList();
		
		allPossibleChanges.ForEach(next =>
		{
			var c = changes.ToList();
			c.Add(next);
			queue.Enqueue((next, c));
		});
	}
	return -1;
}

CalculateTimeExecution("1 - ", () => Console.WriteLine(EditDistance("geek", "gesek")));
CalculateTimeExecution("2 - ", () => Console.WriteLine(EditDistance("gfg", "gfg")));
CalculateTimeExecution("3 - ", () => Console.WriteLine(EditDistance("abcd", "bcfe")));
CalculateTimeExecution("4 - ", () => Console.WriteLine(EditDistance("abcdz", "efghy")));


bool AreEqual(string s1, string s2)
{
	if (s1.Length != s2.Length)
		return false;
	for (var i = 0; i < s1.Length / 2; i++)
	{
		if (s1[i] != s2[i]) return false;
		if (s1[s1.Length - 1 - i] != s2[s1.Length - 1 - i]) return false;
	}
	return true;
}

void CalculateTimeExecution(string message, Action action)
{
	var sw = Stopwatch.StartNew();
	action();
	sw.Stop();
	Console.WriteLine($"{message}: {sw.ElapsedMilliseconds.ToString()}\n");
}