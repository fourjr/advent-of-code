using System;
using System.Collections.Generic;

namespace Day3
{
    class Program
    {
        static void Main()
        {
            string input = System.IO.File.ReadAllText("C:/Users/jiarong/Documents/jr/adventofcode/2020/Day 3/input.txt");
            Console.WriteLine(Part1(input));
            Console.WriteLine(Part2(input));
        }

        static int Part1(string input)
        {
            return Compute(input, 3, 1);
        }

        static uint Part2(string input)
        {
            return (uint)(Compute(input, 1, 1) * Compute(input, 3, 1) * Compute(input, 5, 1) * Compute(input, 7, 1) * Compute(input, 1, 2));
        }

        private static int Compute(string input, int numX, int numY) {
            string[] inputSplit = input.Split("\n");
            List<List<char>> map = new List<List<char>>();
            foreach (string line in inputSplit)
            {
                List<char> row = new List<char>();
                foreach (char c in line)
                {
                    if (c == '#' || c == '.')
                    {
                        row.Add(c);
                    }
                }
                map.Add(row);
            }

            int cursorX = 0;
            int cursorY = 0;
            int count = 0;
            while (cursorY < map.Count) {
                if (map[cursorY][cursorX] == '#')
                {
                    map[cursorY][cursorX] = 'X';
                    count++;
                }
                else
                {
                    map[cursorY][cursorX] = 'O';
                }
                cursorX += numX;
                cursorY += numY;
                if (cursorX >= map[0].Count)
                {
                    cursorX = 0 + cursorX - map[0].Count;
                }
            }

            return count;
        }
    }
}