using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace Day_18
{
    class Program
    {
        static long ParseString(string input, bool orderMatters)
        {
            Regex pattern = new Regex(@"(?<num>\d+)|(?<sign>\+|-|\/|\*)|(?<bracket>\(|\))", RegexOptions.Compiled);
            long sum = 0;
            string[] inputSplit = input.Split("\r\n");
            foreach (string line in inputSplit)
            {
                MatchCollection matches = pattern.Matches(line);
                List<string> items = new List<string>();
                foreach (Match m in matches)
                {

                    GroupCollection groups = m.Groups;
                    if (groups["num"].Value != "")
                    {
                        items.Add(groups["num"].Value);
                    }
                    if (groups["sign"].Value != "")
                    {
                        items.Add(groups["sign"].Value);
                    }
                    if (groups["bracket"].Value != "")
                    {
                        items.Add(groups["bracket"].Value);
                    }
                }
                sum += Calculate(items, orderMatters);
            }
            return sum;
        }

        static long Calculate(List<string> items, bool orderMatters)
        {
            Dictionary<int, int> brackets = new Dictionary<int, int>();
            int bracketStart = -1;
            int skip = 0;
            int skipped = 0;
            for (int i = 0; i < items.Count; i++)
            {
                if (items[i] == "(")
                {
                    if (bracketStart != -1)
                    {
                        skip++;
                    }
                    else
                    {
                        bracketStart = i;
                    }
                }
                if (bracketStart != -1 && items[i] == ")")
                {
                    if (skipped != skip)
                    {
                        skipped++;
                    }
                    else
                    {
                        brackets[bracketStart] = i;
                        bracketStart = -1;
                    }
                }
            }

            Dictionary<int, int> toRemove = new Dictionary<int, int>();

            foreach (KeyValuePair<int, int> val in brackets)
            {
                items[val.Key] = Calculate(items.GetRange(val.Key + 1, val.Value - val.Key - 1), orderMatters).ToString();
                toRemove.Add(val.Key + 1, val.Value - val.Key);
            }

            List<int> keys = new List<int> (toRemove.Keys);
            for(int i = 0; i < keys.Count; i++)
            {
                int key = keys[i];
                items.RemoveRange(key, toRemove[key]);
                for (int ik = 0; ik < keys.Count; ik++)
                {
                    int k = keys[ik];
                    if (k != key)
                    {
                        toRemove[k - toRemove[key]] = toRemove[k];
                        keys.Insert(keys.IndexOf(k), k - toRemove[key]);
                        toRemove.Remove(k);
                        keys.Remove(k);
                    }
                }
            }

            if (orderMatters)
            {
                int ind = 0;
                while ((ind + 1) < items.Count)
                {
                    if (items[ind + 1] == "+")
                    {
                        items[ind] = Equate(long.Parse(items[ind]), long.Parse(items[ind + 2]), items[ind + 1][0]).ToString();
                        items.RemoveRange(ind + 1, 2);
                        ind -= 2;
                    }
                    ind++;
                }
            }

            while (items.Count != 1)
            {
                items[0] = Equate(long.Parse(items[0]), long.Parse(items[2]), items[1][0]).ToString();
                items.RemoveRange(1, 2);
            }
            return long.Parse(items[0]);
        }
        static long Equate(long x, long y, char sign)
        {
            switch (sign)
            {
                case '+':
                    return x + y;
                case '*':
                    return x * y;
                default:
                    throw new Exception($"Unspported sign: {sign}");
            }
        }
        static void Main(string[] args)
        {
            string input = System.IO.File.ReadAllText("../../../input.txt");

            // Part 1
            Console.WriteLine(ParseString(input, false));
            // Part 2
            Console.WriteLine(ParseString(input, true));
        }
    }
}
