using System;

namespace Day_12
{
    class Program
    {
        static void Main()
        {
            string input = System.IO.File.ReadAllText("../../../input.txt");
            Console.WriteLine(Part1(input));
            Console.WriteLine(Part2(input));
        }

        static int Part1(string input) {
            string[] inputSplit = input.Split("\r\n");
            int northPos = 0;
            int eastPos = 0;
            int facing = 90;
            foreach (string line in inputSplit)
            {
                int value = int.Parse(line.Substring(1));
                switch (line[0])
                {
                    case 'N':
                        northPos += value;
                        break;
                    case 'S':
                        northPos -= value;
                        break;
                    case 'E':
                        eastPos += value;
                        break;
                    case 'W':
                        eastPos -= value;
                        break;
                    case 'F':
                        if (facing == 0)
                        {
                            goto case 'N';
                        }
                        else if (facing == 90)
                        {
                            goto case 'E';
                        }
                        else if (facing == 180)
                        {
                            goto case 'S';
                        }
                        else if (facing == 270)
                        {
                            goto case 'W';
                        }
                        else
                        {
                            Console.WriteLine($"Invalid facing: {facing}");
                        }
                        break;
                    case 'L':
                        facing -= value;
                        if (facing < 0)
                        {
                            facing = 360 - Math.Abs(facing);
                        }
                        facing %= 360;
                        break;
                    case 'R':
                        facing += value;
                        facing %= 360;
                        if (facing < 0)
                        {
                            facing = 360 - Math.Abs(facing);
                        }
                        facing %= 360;
                        break;
                }
            }
            return Math.Abs(northPos) + Math.Abs(eastPos);
        }

        static int Part2(string input)
        {
            string[] inputSplit = input.Split("\r\n");
            int shipNorthPos = 0;
            int shipEastPos = 0;
            int northPos = 1;
            int eastPos = 10;
            foreach (string line in inputSplit)
            {
                int value = int.Parse(line.Substring(1));
                int temp;
                switch (line[0])
                {
                    case 'N':
                        northPos += value;
                        break;
                    case 'S':
                        northPos -= value;
                        break;
                    case 'E':
                        eastPos += value;
                        break;
                    case 'W':
                        eastPos -= value;
                        break;
                    case 'F':
                        shipNorthPos += northPos * value;
                        shipEastPos += eastPos * value;
                        break;
                    case 'L':
                        switch (value)
                        {
                            case 90:
                                temp = northPos;
                                northPos = eastPos;
                                eastPos = -temp;
                                break;
                            case 180:
                                northPos *= -1;
                                eastPos *= -1;
                                break;
                            case 270:
                                temp = northPos;
                                northPos = -eastPos;
                                eastPos = temp;
                                break;
                            default:
                                Console.WriteLine($"Invalid value: {value}");
                                break;
                        }
                        break;
                    case 'R':
                        switch (value)
                        {
                            case 90:
                                temp = northPos;
                                northPos = -eastPos;
                                eastPos = temp;
                                break;
                            case 180:
                                northPos *= -1;
                                eastPos *= -1;
                                break;
                            case 270:
                                temp = northPos;
                                northPos = eastPos;
                                eastPos = -temp;
                                break;
                            default:
                                Console.WriteLine($"Invalid value: {value}");
                                break;
                        }
                        break;
                }
            }
            return Math.Abs(shipNorthPos) + Math.Abs(shipEastPos);
        }
    }
}
