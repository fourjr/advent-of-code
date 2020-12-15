using System;
using System.Collections.Generic;

namespace Day_15
{
    class Program
    {
        static void Main()
        {
            string input = System.IO.File.ReadAllText("../../../input.txt");
            // Part 1
            Console.WriteLine(Calculate(input, 2020));
            // Part 2
            Console.WriteLine(Calculate(input, 30000000));
        }

        static int Calculate(string input, int target) {
            List<int> numbers = new List<int>();
            Dictionary<int, List<int>> values = new Dictionary<int, List<int>>();
            foreach (string x in input.Split(","))
            {
                int toAdd = int.Parse(x);
                numbers.Add(toAdd);
                if (values.ContainsKey(toAdd))
                {
                    values[toAdd].Add(numbers.Count - 1);
                }
                else
                {
                    values[toAdd] = new List<int>() { numbers.Count - 1 };
                }
            }

            while (numbers.Count < target)
            {
                int toAdd;
                int toFind = numbers[numbers.Count - 1];
                List<int> big = values[toFind];
                if (values.ContainsKey(toFind) && big.Count > 1)
                {
                    toAdd = big[big.Count - 1] - big[big.Count - 2];
                }
                else
                {
                    toAdd = 0;
                }

                numbers.Add(toAdd);
                if (values.ContainsKey(toAdd))
                {
                    values[toAdd].Add(numbers.Count - 1);
                }
                else
                {
                    values[toAdd] = new List<int>() { numbers.Count - 1 };
                }
            }
            return numbers[numbers.Count - 1];
        }
    }
}
