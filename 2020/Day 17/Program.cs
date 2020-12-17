using System;
using System.Collections.Generic;
using System.Linq;

namespace Day_17
{
    class Program
    {
        static int GetNeighbours(SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>> map, int _x, int _y, int _z)
        {
            char target = '#';

            int sum = 0;
            for (int z = _z - 1; z <= _z + 1; z++)
            {
                if (!map.ContainsKey(z))
                {
                    continue;
                }
                for (int y = _y - 1; y <= _y + 1; y++)
                {
                    if (!map[z].ContainsKey(y))
                    {
                        continue;
                    }
                    for (int x = _x - 1; x <= _x + 1; x++)
                    {
                        char position;
                        if (!map[z][y].ContainsKey(x))
                        {
                            continue;
                        }
                        if (_z == z && _y == y && _x == x)
                        {
                            continue;
                        }
                        position = map[z][y][x];

                        if (position == target)
                        {
                            sum++;
                        }
                    }
                }
            }

            return sum;
        }
        static int GetNeighbours(SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>>> map, int _x, int _y, int _z, int _w)
        {
            char target = '#';

            int sum = 0;
            for (int w = _w - 1; w <= _w + 1; w++)
            {
                if (!map.ContainsKey(w))
                {
                    continue;
                }
                for (int z = _z - 1; z <= _z + 1; z++)
                {
                    if (!map[w].ContainsKey(z))
                    {
                        continue;
                    }
                    for (int y = _y - 1; y <= _y + 1; y++)
                    {
                        if (!map[w][z].ContainsKey(y))
                        {
                            continue;
                        }
                        for (int x = _x - 1; x <= _x + 1; x++)
                        {
                            char position;
                            if (!map[w][z][y].ContainsKey(x))
                            {
                                continue;
                            }
                            if (_w == w && _z == z && _y == y && _x == x)
                            {
                                continue;
                            }
                            position = map[w][z][y][x];

                            if (position == target)
                            {
                                sum++;
                            }
                        }
                    }
                }
            }

            return sum;
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
            SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>> map = new SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>>();
            //map[z][y][x]
            map[0] = new SortedDictionary<int, SortedDictionary<int, char>>();

            int yVal = 0;
            foreach (string line in inputSplit)
            {
                SortedDictionary<int, char> xValues = new SortedDictionary<int, char>();
                for (int x = 0; x < line.Length; x++)
                {
                    xValues[x] = line[x];
                }
                map[0].Add(yVal, xValues);
                yVal++;
            }

            //Cycle simulation
            for (int i = 0; i < 6; i++)
            {
                List<int> zKeys = new List<int>(map.Keys);
                zKeys.Insert(0, zKeys.Min() - 1);
                zKeys.Add(zKeys.Max() + 1);

                List<int> yKeys = new List<int>(map[0].Keys);
                yKeys.Insert(0, yKeys.Min() - 1);
                yKeys.Add(yKeys.Max() + 1);

                List<int> xKeys = new List<int>(map[0][0].Keys);
                xKeys.Insert(0, xKeys.Min() - 1);
                xKeys.Add(xKeys.Max() + 1);

                SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>> newMap = new SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>>();

                foreach (int z in map.Keys)
                {
                    newMap[z] = new SortedDictionary<int, SortedDictionary<int, char>>();
                    foreach (int y in map[z].Keys)
                    {
                        newMap[z][y] = new SortedDictionary<int, char>();
                        foreach (int x in map[z][y].Keys)
                        {
                            newMap[z][y][x] = map[z][y][x].ToString()[0];
                        }
                    }
                }


                foreach (int z in zKeys)
                {
                    if (!newMap.ContainsKey(z))
                    {
                        newMap[z] = new SortedDictionary<int, SortedDictionary<int, char>>();
                    }
                    foreach (int y in yKeys)
                    {
                        if (!newMap[z].ContainsKey(y))
                        {
                            newMap[z][y] = new SortedDictionary<int, char>();
                        }
                        foreach (int x in xKeys)
                        {
                            if (!newMap[z][y].ContainsKey(x))
                            {
                                newMap[z][y][x] = '.';
                            }
                            char position;
                            try
                            {
                                position = map[z][y][x];
                            }
                            catch (KeyNotFoundException)
                            {
                                position = '.';
                            }

                            int neighbours = GetNeighbours(map, x, y, z);
                            if (position == '#')
                            {
                                if (neighbours != 2 && neighbours != 3)
                                {
                                    newMap[z][y][x] = '.';
                                }
                            }
                            else if (position == '.')
                            {
                                if (neighbours == 3)
                                {
                                    newMap[z][y][x] = '#';
                                }
                            }
                        }
                    }
                }
                map = new SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>>(newMap);
            }

            int sum = 0;
            foreach (int z in map.Keys)
            {
                foreach (int y in map[z].Keys)
                {
                    foreach (int x in map[z][y].Keys)
                    {
                        char position = map[z][y][x];
                        if (position == '#')
                        {
                            sum++;
                        }
                    }
                }
            }
            return sum;
        }

        static int Part2(string input) {
            string[] inputSplit = input.Split("\r\n");
            SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>>> map = new SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>>>();
            //map[w][z][y][x]
            map[0] = new SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>>
            {
                [0] = new SortedDictionary<int, SortedDictionary<int, char>>()
            };

            int yVal = 0;
            foreach (string line in inputSplit)
            {
                SortedDictionary<int, char> xValues = new SortedDictionary<int, char>();
                for (int x = 0; x < line.Length; x++)
                {
                    xValues[x] = line[x];
                }
                map[0][0].Add(yVal, xValues);
                yVal++;
            }

            //Cycle simulation
            for (int i = 0; i < 6; i++)
            {
                List<int> wKeys = new List<int>(map.Keys);
                wKeys.Insert(0, wKeys.Min() - 1);
                wKeys.Add(wKeys.Max() + 1);

                List<int> zKeys = new List<int>(map[0].Keys);
                zKeys.Insert(0, zKeys.Min() - 1);
                zKeys.Add(zKeys.Max() + 1);

                List<int> yKeys = new List<int>(map[0][0].Keys);
                yKeys.Insert(0, yKeys.Min() - 1);
                yKeys.Add(yKeys.Max() + 1);

                List<int> xKeys = new List<int>(map[0][0][0].Keys);
                xKeys.Insert(0, xKeys.Min() - 1);
                xKeys.Add(xKeys.Max() + 1);

                SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>>> newMap = new SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>>>();

                foreach (int w in map.Keys) {
                    newMap[w] = new SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>>();
                    foreach (int z in map[w].Keys)
                    {
                        newMap[w][z] = new SortedDictionary<int, SortedDictionary<int, char>>();
                        foreach (int y in map[w][z].Keys)
                        {
                            newMap[w][z][y] = new SortedDictionary<int, char>();
                            foreach (int x in map[w][z][y].Keys)
                            {
                                newMap[w][z][y][x] = map[w][z][y][x].ToString()[0];
                            }
                        }
                    }
                }

                foreach (int w in wKeys)
                {
                    if (!newMap.ContainsKey(w))
                    {
                        newMap[w] = new SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>>();
                    }
                    foreach (int z in zKeys)
                    {
                        if (!newMap[w].ContainsKey(z))
                        {
                            newMap[w][z] = new SortedDictionary<int, SortedDictionary<int, char>>();
                        }
                        foreach (int y in yKeys)
                        {
                            if (!newMap[w][z].ContainsKey(y))
                            {
                                newMap[w][z][y] = new SortedDictionary<int, char>();
                            }
                            foreach (int x in xKeys)
                            {
                                if (!newMap[w][z][y].ContainsKey(x))
                                {
                                    newMap[w][z][y][x] = '.';
                                }
                                char position;
                                try
                                {
                                    position = map[w][z][y][x];
                                }
                                catch (KeyNotFoundException)
                                {
                                    position = '.';
                                }

                                int neighbours = GetNeighbours(map, x, y, z, w);
                                if (position == '#')
                                {
                                    if (neighbours != 2 && neighbours != 3)
                                    {
                                        newMap[w][z][y][x] = '.';
                                    }
                                }
                                else if (position == '.')
                                {
                                    if (neighbours == 3)
                                    {
                                        newMap[w][z][y][x] = '#';
                                    }
                                }
                            }
                        }
                    }
                }
                map = new SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, SortedDictionary<int, char>>>>(newMap);
            }

            int sum = 0;
            foreach (int w in map.Keys) {
                foreach (int z in map[w].Keys)
                {
                    foreach (int y in map[w][z].Keys)
                    {
                        foreach (int x in map[w][z][y].Keys)
                        {
                            char position = map[w][z][y][x];
                            if (position == '#')
                            {
                                sum++;
                            }
                        }
                    }
                }
            }
            return sum;
        }
    }
}
