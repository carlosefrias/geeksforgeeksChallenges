int CountPS(string s)
{
	if (s.Length < 2)
		return 0;
	var palindromes = new List<string>();
	for (int length = 2; length < s.Length; length++)
	{
		var pos = 0;
		while (pos + length <= s.Length)
		{
			var subString = s.Substring(pos, length);
			if(IsPalindrome(subString))
				palindromes.Add(subString);
			pos++;
		}
	}

	return palindromes.Count;
}

bool IsPalindrome(string s)
{
	var reverse = string.Join("", s.Reverse());
	return s.Equals(reverse);
}

// See https://aka.ms/new-console-template for more information

Console.WriteLine(CountPS("abaab"));
Console.WriteLine(CountPS("aaa"));
Console.WriteLine(CountPS("abbaeae"));