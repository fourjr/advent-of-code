using System;
using System.Collections.Generic;

namespace Day_8
{
    class Program
    {
        static void Main()
        {
            string text = System.IO.File.ReadAllText("C:/Users/jiarong/Documents/jr/adventofcode/2020/Day 8/input.txt");
            string[] splitText = text.Split("\r\n");

            // Part 1
            BootCode bc = new BootCode(splitText);
            Console.WriteLine(bc.Execute());
            // Part 2
            BootCodeFix bcf = new BootCodeFix(splitText);
            Console.WriteLine(bcf.Fix());
        }
    }
}
