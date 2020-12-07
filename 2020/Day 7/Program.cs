using System;
using System.Collections.Generic;
using System.Linq;

namespace Day_7
{
    class Program
    {
        private static Dictionary<string, List<Tuple<string, int>>> bags = new Dictionary<string, List<Tuple<string, int>>>();

        static HashSet<string> CanContain(string color)
        {
            HashSet<string> total = new HashSet<string>();
            foreach (KeyValuePair<string, List<Tuple<string, int>>> val in bags)
            {
                foreach (Tuple<string, int> b in val.Value)
                {
                    if (b.Item1 == color)
                    {
                        total.Add(val.Key);
                        total.UnionWith(CanContain(val.Key));
                    }
                }
            }
            return total;
        }

        static int CountInside(string color)
        {
            int count = 0;
            foreach (KeyValuePair<string, List<Tuple<string, int>>> val in bags)
            {
                if (val.Key == color) {
                    foreach (Tuple<string, int> b in val.Value)
                    {
                        count += b.Item2 + CountInside(b.Item1) * b.Item2;
                    }
                }
            }
            return count;
        }

        static void Main()
        {
            string input = System.IO.File.ReadAllText("C:/Users/jiarong/Documents/jr/adventofcode/2020/Day 7/input.txt");

            // Preprocessing shared across both parts
            foreach (string line in input.Split("\r\n"))
            {
                string[] bagName = line.Split(" contain ");
                bags[bagName[0].Split(" bags")[0]] = new List<Tuple<string, int>>();
                foreach (string x in bagName[1].Split(", "))
                {
                    if (x != "no other bags.")
                    {
                        string[] cutspace = x.Split(" ");
                        string[] newcut = new string[cutspace.Length - 2];

                        // super scuffed string.splice (its essentially cutspace[1:-1] in python)
                        int n = 0;
                        foreach (string c in cutspace) { 
                            if (n != 0 && n != cutspace.Length - 1)
                            {
                                newcut[n - 1] = c;
                            }
                            n++;
                        }
                        string name = string.Join(" ", newcut);
                        int no = int.Parse(cutspace[0]);
                        bags[bagName[0].Split(" bags")[0]].Add(new Tuple<string, int>(name, no));
                    }
                }
            }

            // Part 1
            Console.WriteLine(CanContain("shiny gold").Count);

            // Part 2
            Console.WriteLine(CountInside("shiny gold"));
        }
    }
}
