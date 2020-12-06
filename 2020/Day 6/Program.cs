using System;
using System.Collections.Generic;

namespace Day6
{
    class Program
    {
        static void Main()
        {
            string input = System.IO.File.ReadAllText("C:/Users/jiarong/Documents/jr/adventofcode/2020/Day 6/input.txt");
            Console.WriteLine(Part1(input));
            Console.WriteLine(Part2(input));
        }

        static int Part1(string input)
        {
            string[] inputSplit = input.Split("\r\n\r\n");
            int totalCount = 0;

            foreach (string line in inputSplit)
            {
                HashSet<char> responses = new HashSet<char>();
                foreach (string ll in line.Split("\r\n"))
                {
                    foreach (char c in ll)
                    {
                        responses.Add(c);
                    }
                }
                totalCount += responses.Count;
            }
            return totalCount;
        }

        static int Part2(string input)
        {
            string[] inputSplit = input.Split("\r\n\r\n");
            int totalCount = 0;

            foreach (string line in inputSplit)
            {
                Dictionary<char, int> hasKey = new Dictionary<char, int>();
                int n = 0;
                foreach (string ll in line.Split("\r\n"))
                {
                    foreach (char c in ll)
                    {
                        if (n == 0)
                        {
                            hasKey.Add(c, 1);
                        }
                        else
                        {
                            if (hasKey.ContainsKey(c))
                            {
                                hasKey[c] += 1;
                            }
                        }
                    }
                    n++;
                }
                foreach (KeyValuePair<char, int> entry in hasKey)
                {
                    if (entry.Value == n)
                    {
                        totalCount += 1;
                    }
                }
            }
            return totalCount;
        }
    }
}
