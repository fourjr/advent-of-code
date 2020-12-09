using System;
using System.Collections.Generic;

namespace Day_9
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = System.IO.File.ReadAllText("C:/Users/jiarong/Documents/jr/adventofcode/2020/Day 9/input.txt");

            // Shared preprocessing
            List<long> numbers = new List<long>();
            foreach (string i in input.Split("\r\n"))
            {
                numbers.Add(long.Parse(i));
            }

            Console.WriteLine(Part1(numbers));
            Console.WriteLine(Part2(numbers));
        }

        static long Part1(List<long> numbers)
        {
            for (int i = 50; i < numbers.Count; i++)
            {
                bool success = false;
                for (int j = i - 50; j < i; j++)
                {
                    for (int h = i - 50; h < i; h++)
                    {
                        if (j != h)
                        {
                            if (numbers[j] + numbers[h] == numbers[i])
                            {
                                success = true;
                                break;
                            }
                        }
                    }
                    if (success)
                    {
                        break;
                    }
                }
                if (!success)
                {
                    return numbers[i];
                }
            }
            throw new Exception("Invalid data, cannot find first anomaly");
        }

        static long Part2(List<long> numbers) {
            long target = 507622668;
            for (int i = 0; i < numbers.Count; i++)
            {
                long min = numbers[i];
                long max = numbers[i];
                long sum = numbers[i];
                for (int j = i + 1; j < numbers.Count; j++)
                {
                    sum += numbers[j];
                    if (min > numbers[j])
                    {
                        min = numbers[j];
                    }
                    if (max < numbers[j])
                    {
                        max = numbers[j];
                    }

                    if (sum == target)
                    {
                        return min + max;
                    }
                    if (sum > target)
                    {
                        break;
                    }
                }
            }
            throw new Exception("Invalid data, cannot find encryption weakness");
        }
    }
}
