using System;
using System.Collections.Generic;

namespace Day2
{
    class Program
    {
        static void Main()
        {
            string input = System.IO.File.ReadAllText("C:/Users/jiarong/Documents/jr/adventofcode/2020/Day 2/input.txt");
            Console.WriteLine(Part1(input));
            Console.WriteLine(Part2(input));
        }

        static int Part1(string input)
        {
            string[] inputSplit = input.Split("\n");
            int valid = 0;
            foreach (string line in inputSplit)
            {
                string[] sections = line.Split(" ");
                string[] parameters = sections[0].Split("-");
                List<int> realParam = new List<int>();
                foreach (string p in parameters)
                {
                    realParam.Add(int.Parse(p));
                }

                char letter = sections[1].ToCharArray()[0];
                string fullword = sections[2];

                int count = 0;
                foreach (char c in fullword)
                {
                    if (c == letter)
                    {
                        count++;
                    }
                }

                if (count >= realParam[0] && count <= realParam[1])
                {
                    valid += 1;
                }
            }

            return valid;
        }

        static int Part2(string input) {
            string[] inputSplit = input.Split("\n");
            int valid = 0;

            foreach (string line in inputSplit)
            {
                string[] sections = line.Split(" ");
                string[] parameters = sections[0].Split("-");
                char letter = sections[1].ToCharArray()[0];
                string fullword = sections[2];

                int count = 0;
                foreach (string p in parameters)
                {
                    int index = int.Parse(p) - 1;
                    if (fullword[index] == letter)
                    {
                        count += 1;
                    }
                }
                if (count == 1)
                {
                    valid += 1;
                }
            }

            return valid;
        }
    }
}
