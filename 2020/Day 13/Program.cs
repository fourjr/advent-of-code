using System;
using System.Collections.Generic;

namespace Day_13
{
    class Program
    {
        static void Main()
        {
            string input = System.IO.File.ReadAllText("../../../input.txt");
            Console.WriteLine(Part1(input));
            Console.WriteLine(Part2(input));
        }

        static int Part1(string input)
        {
            string[] inputSplit = input.Split("\r\n");
            int desiredTime = int.Parse(inputSplit[0]);
            string[] busesStr = inputSplit[1].Split(",");
            List<int> buses = new List<int>();
            foreach (string b in busesStr)
            {
                if (b != "x")
                {
                    buses.Add(int.Parse(b));
                }
            }

            int n = desiredTime;
            while (true)
            {
                foreach (int x in buses)
                {
                    if (n % x == 0)
                    {
                        return x * (n - desiredTime);
                    }
                }
                n++;
            }
        }

        static long Part2(string input) {
            // didnt work
            string[] inputSplit = input.Split("\r\n");
            string[] busesStr = inputSplit[1].Split(",");
            Dictionary<long, long> buses = new Dictionary<long, long>();
            long nn = 0;
            foreach (string b in busesStr)
            {
                if (b != "x")
                {
                    buses[nn] = long.Parse(b);
                }
               nn++;
            }

            long n = 0;
            while (true)
            {
                if (n % buses[0] == 0)
                {
                    int counter = 0;
                    foreach (KeyValuePair<long, long> b in buses)
                    {
                        if (b.Key != 0)
                        {
                            if ((n + b.Key) % b.Value != 0)
                            {
                                break;
                            }
                        }

                        if (counter == buses.Count - 1)
                        {
                            return n;
                        }
                        counter++;
                    }
                    n += buses[0] - 1;
                }
                n++;
            }
        }
    }
}
