using System;
using System.Linq;
using System.Collections.Generic;

namespace Day_10
{
    class Program
    {
        static readonly List<int> ratings = new List<int>();
        static int? _maxR = null;
        static int MaxR { get
            {
                if (_maxR == null)
                {
                    _maxR = ratings.Max();
                }
                return (int)_maxR;
            } }
        static ulong totalPossible = 0;
        static readonly Dictionary<int, ulong> calculated = new Dictionary<int, ulong>();

        static int Part1()
        {
            int minRange = 0;
            int oneJolt = 0;
            int threeJolt = 1;
            foreach (int r in ratings)
            {
                if (r - minRange > 0 && 3 >= (r - minRange))
                {
                    if ((r - minRange) == 1)
                    {
                        oneJolt++;
                    }
                    if ((r - minRange) == 3)
                    {
                        threeJolt++;
                    }
                    minRange = r;
                }
            }
            return oneJolt * threeJolt;
        }

        static ulong Part2(int minRange=0)
        {
            if (calculated.ContainsKey(minRange))
            {
                // Optimisation: skip whole recursion if this number has already been counted
                totalPossible += calculated[minRange];
                return totalPossible;
            }

            ulong preRun = totalPossible;
            if (minRange == MaxR)
            {
                totalPossible++;
            }
            foreach (int r in ratings)
            {
                if (r - minRange > 0 && 3 >= (r - minRange))
                {
                    Part2(r);
                }
            }
            calculated[minRange] = totalPossible - preRun; // save difference of totalPossible
            return totalPossible;
        }

        static void Main()
        {
            string input = System.IO.File.ReadAllText("C:/Users/jiarong/Documents/jr/adventofcode/2020/Day 10/input.txt");
            string[] inputSplit = input.Split("\r\n");
            // Shared preprocessing
            foreach (string line in inputSplit)
            {
                ratings.Add(int.Parse(line));
            }
            ratings.Sort();

            Console.WriteLine(Part1());
            Console.WriteLine(Part2());
        }
    }
}
