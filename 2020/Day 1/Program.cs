using System;

namespace Day1
{
    class Program
    {
        static void Main()
        {
            string input = System.IO.File.ReadAllText("input.txt");
            Console.WriteLine(Part1(input));
            Console.WriteLine(Part2(input));
        }

        static int Part1(string input)
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
                            return intVal * intVal2;
                        }
                    }
                }
            }
            throw new Exception("Invalid input");
        }
        static int Part2(string input)
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
                                    return intVal * intVal2 * intVal3;
                                }
                            }
                        }
                    }
                }
            }
            throw new Exception("Invalid input")
        }
    }
}