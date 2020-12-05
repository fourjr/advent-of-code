using System;
using System.Collections.Generic;

namespace Day_5
{
    class Program
    {
        static void Main()
        {
            string input = System.IO.File.ReadAllText("C:/Users/jiarong/Documents/jr/adventofcode/2020/Day 5/input.txt");
            Console.WriteLine(Part1(input));
            Console.WriteLine(Part2(input));
        }

        static int Part1(string input)
        {
            string[] inputSplit = input.Split("\r\n");
            int maxId = 0;

            foreach (string code in inputSplit)
            {
                int id = GetId(code);
                if (maxId < id)
                {
                    maxId = id;
                }
            }
            return maxId;
        }

        static int Part2(string input)
        {
            string[] inputSplit = input.Split("\r\n");
            int maxId = 0;
            List<int> ids = new List<int>();

            foreach (string code in inputSplit)
            {
                ids.Add(GetId(code));
            }

            int maxSeat = Part1(input);
            for (int i = 0; i < maxSeat; i++)
            {
                if (!ids.Contains(i) && maxId < i)
                {
                    maxId = i;
                }
            }
            return maxId;
        }

        static int GetId(string code)
        {
            double minRow = 0;
            double maxRow = 127;
            double minColumn = 0;
            double maxColumn = 7;
            foreach (char c in code)
            {
                switch (c)
                {
                    case 'F':
                        maxRow = Math.Floor((float)((maxRow - minRow) / 2 + minRow));
                        break;
                    case 'B':
                        minRow += Math.Ceiling((float)((maxRow - minRow) / 2));
                        break;
                    case 'R':
                        minColumn += Math.Ceiling((float)((maxColumn - minColumn) / 2));
                        break;
                    case 'L':
                        maxColumn = Math.Floor((float)((maxColumn - minColumn) / 2 + minColumn));
                        break;
                }
            }
            if (maxRow != minRow || maxColumn != minColumn)
            {
                Console.WriteLine($"error with {code}");
            }

            return (int)(maxRow * 8 + maxColumn);
        }
    }
}