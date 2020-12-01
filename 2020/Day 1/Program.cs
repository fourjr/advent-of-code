using System;

namespace Day1
{
    class Program
    {
        static void Main()
        {
            string input = System.IO.File.ReadAllText("C:/Users/jiarong/Documents/jr/adventofcode/2020/Day 1/input.txt");
            Part1(input);
            Part2(input);
        }

        static void Part1(string input)
        {
            string[] inputSplit = input.Split("\n");
            foreach (string x in inputSplit)
            {
                int intVal = int.Parse(x);
                foreach (string y in inputSplit)
                {
                    if (x != y)
                    {
                        int intVal2 = int.Parse(y);
                        if (intVal + intVal2 == 2020)
                        {
                            Console.WriteLine(intVal * intVal2);
                            return;
                        }
                    }
                }
            }
        }
        static void Part2(string input)
        {
            string[] inputSplit = input.Split("\n");
            foreach (string x in inputSplit)
            {
                int intVal = int.Parse(x);
                foreach (string y in inputSplit)
                {
                    if (x != y)
                    {
                        int intVal2 = int.Parse(y);
                        foreach (string z in inputSplit)
                        {
                            if (x != y && y != z && x != z)
                            {
                                int intVal3 = int.Parse(z);
                                if (intVal + intVal2 + intVal3 == 2020)
                                {
                                    Console.WriteLine(intVal * intVal2 * intVal3);
                                    return;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}