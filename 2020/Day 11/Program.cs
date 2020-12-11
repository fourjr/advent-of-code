using System;
using System.Collections.Generic;
using System.Linq;

namespace Day_11
{
    class Program
    {
        static List<List<char>> previousSeats;
        static List<List<char>> seats;
        static char GetAdjacent(int cRow, int cColumn, int rOffset, int cOffset)
        {
            int row = cRow + rOffset;
            int column = cColumn + cOffset;
            while (row >= 0 && row < seats.Count && column >= 0 && column < seats[row].Count)
            {
                if (previousSeats[row][column] != '.')
                {
                    return previousSeats[row][column];
                }
                row += rOffset;
                column += cOffset;
            }
            return '.';
        }
        static char GetSeat(int row, int column)
        {
            if (row >= 0 && row < seats.Count)
            {
                if (column >= 0 && column < seats[row].Count)
                {
                    return previousSeats[row][column];
                }
            }
            return '.';
        }
        static void Main(string[] args)
        {
            string input = System.IO.File.ReadAllText("../../../input.txt");

            Console.WriteLine(Part1(input));
            Console.WriteLine(Part2(input));
        }
        static int Part1(string input)
        {
            string[] inputSplit = input.Split("\r\n");
            seats = new List<List<char>>();
            foreach (string line in inputSplit)
            {
                List<char> thisRow = new List<char>();
                foreach (char c in line)
                {
                    thisRow.Add(c);
                }
                seats.Add(thisRow);
            }
            while (true)
            {
                previousSeats = new List<List<char>>();
                foreach (List<char> rrrr in seats)
                {
                    List<char> rowL = new List<char>();
                    foreach (char cccc in rrrr)
                    {
                        rowL.Add(cccc);
                    }
                    previousSeats.Add(rowL);
                }

                for (int row = 0; row < seats.Count; row++)
                {
                    for (int column = 0; column < seats[row].Count; column++)
                    {
                        char c = seats[row][column];
                        if (c == 'L' &&
                            GetSeat(row, column + 1) != '#' &&
                            GetSeat(row, column - 1) != '#' &&
                            GetSeat(row + 1, column) != '#' &&
                            GetSeat(row - 1, column) != '#' &&
                            GetSeat(row + 1, column + 1) != '#' &&
                            GetSeat(row + 1, column - 1) != '#' &&
                            GetSeat(row - 1, column + 1) != '#' &&
                            GetSeat(row - 1, column - 1) != '#')
                        {
                            seats[row][column] = '#';
                        }
                        if (c == '#')
                        {
                            List<char> counter = new List<char>() {
                                GetSeat(row, column + 1),
                                GetSeat(row, column - 1),
                                GetSeat(row + 1, column),
                                GetSeat(row - 1, column),
                                GetSeat(row + 1, column + 1),
                                GetSeat(row + 1, column - 1),
                                GetSeat(row - 1, column + 1),
                                GetSeat(row - 1, column - 1),
                            };
                            int count = 0;
                            foreach (char cccc in counter)
                            {
                                if (cccc == '#')
                                {
                                    count++;
                                }
                            }

                            if (count >= 4)
                            {
                                seats[row][column] = 'L';
                            }
                        }
                    }
                }

                int desiredCount = seats.Count * seats[0].Count;
                int sameCount = 0;
                for (int r = 0; r < seats.Count; r++)
                {
                    for (int c = 0; c < seats[r].Count; c++)
                    {
                        if (seats[r][c] == previousSeats[r][c])
                        {
                            sameCount++;
                        }
                    }
                }
                if (sameCount == desiredCount)
                {
                    int finalCount = 0;
                    foreach (List<char> r in seats)
                    {
                        foreach (char c in r)
                        {
                            if (c == '#')
                            {
                                finalCount++;
                            }
                        }
                    }
                    return finalCount;
                }
            }
        }

        static int Part2(string input) {
            string[] inputSplit = input.Split("\r\n");
            seats = new List<List<char>>();
            foreach (string line in inputSplit)
            {
                List<char> thisRow = new List<char>();
                foreach (char c in line)
                {
                    thisRow.Add(c);
                }
                seats.Add(thisRow);
            }
            while (true)
            {
                previousSeats = new List<List<char>>();
                foreach (List<char> rrrr in seats)
                {
                    List<char> rowL = new List<char>();
                    foreach (char cccc in rrrr)
                    {
                        rowL.Add(cccc);
                    }
                    previousSeats.Add(rowL);
                }

                for (int row = 0; row < seats.Count; row++)
                {
                    for (int column = 0; column < seats[row].Count; column++)
                    {
                        char c = seats[row][column];
                        if (c == 'L' &&
                            GetAdjacent(row, column, 0  , + 1) != '#' && 
                            GetAdjacent(row, column, 0  , - 1) != '#' && 
                            GetAdjacent(row, column, + 1, 0) != '#' && 
                            GetAdjacent(row, column, - 1, 0) != '#' &&
                            GetAdjacent(row, column, + 1, + 1) != '#' &&
                            GetAdjacent(row, column, + 1, - 1) != '#' &&
                            GetAdjacent(row, column, - 1, + 1) != '#' &&
                            GetAdjacent(row, column, - 1, - 1) != '#')
                        {
                            seats[row][column] = '#';
                        }
                        if (c == '#')
                        {
                            List<char> counter = new List<char>() {
                                GetAdjacent(row, column, 0, + 1),
                                GetAdjacent(row, column, 0, - 1),
                                GetAdjacent(row, column, + 1, 0),
                                GetAdjacent(row, column, - 1, 0),
                                GetAdjacent(row, column, + 1, + 1),
                                GetAdjacent(row, column, + 1, - 1),
                                GetAdjacent(row, column, - 1, + 1),
                                GetAdjacent(row, column, - 1, - 1),
                            };
                            int count = 0;
                            foreach (char cccc in counter)
                            {
                                if (cccc == '#')
                                {
                                    count++;
                                }
                            }

                            if (count >= 5)
                            {
                                seats[row][column] = 'L';
                            }
                        }
                    }
                }

                int desiredCount = seats.Count * seats[0].Count;
                int sameCount = 0;
                for (int r = 0; r < seats.Count; r++)
                {
                    for (int c = 0; c < seats[r].Count; c++)
                    {
                        if (seats[r][c] == previousSeats[r][c])
                        {
                            sameCount++;
                        }
                    }
                }
                if (sameCount == desiredCount) {
                    int finalCount = 0;
                    foreach (List<char> r in seats)
                    {
                        foreach (char c in r)
                        {
                            if (c == '#')
                            {
                                finalCount++;
                            }
                        }
                    }
                    return finalCount;
                }
            }
        }
    }
}
