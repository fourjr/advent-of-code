using System;
using System.Collections.Generic;
using System.Linq;

namespace Day_20
{
    /*
     * This is slow
     * Really slow
     * Haven't got part 1
     */

    public class Pixel
    {
        public int id;
        public List<string> data;
        public List<string> defaultData;
        public Pixel(string _data)
        {
            string[] split = _data.Split("\r\n");
            id = int.Parse(split[0].Substring(5).Substring(0, split[0].Substring(5).Length - 1));

            data = new List<string>(split.Skip(1));
            defaultData = new List<string>(split.Skip(1));
        }

        public void Rotate()
        {
            data.Reverse();
        }

        public void Flip()
        {
            List<string> newData = new List<string>();
            foreach (string d in data)
            {
                newData.Add(string.Join("", d.Reverse().ToArray()));
            }

            data = newData;
        }

        public string GetTop()
        {
            return data[0];
        }
        public string GetBottom()
        {
            return data[^1];
        }

        public string GetLeft()
        {
            string val = "";

            foreach (string d in data)
            {
                val += d[0];
            }

            return val;
        }

        public string GetRight()
        {
            string val = "";

            foreach (string d in data)
            {
                val += d[^1];
            }

            return val;
        }

        public void Reset()
        {
            data = defaultData;
        }
    }

    class Program
    {
        static void Main()
        {
            string input = System.IO.File.ReadAllText("../../../input.txt");
            string[] inputSplit = input.Split("\r\n\r\n");
            List<Pixel> map = new List<Pixel>();

            foreach (string line in inputSplit)
            {
                Pixel pixelData = new Pixel(line);
                map.Add(pixelData);
            }
            int size = (int)Math.Sqrt(map.Count);

            List<List<Pixel>> image = new List<List<Pixel>>();

            int count = 0;
            for (int i = 0; i < size; i++)
            {
                image.Add(new List<Pixel>());
                for (int j = 0; j < size; j++)
                {
                    image[i].Add(map[count]);
                    count++;
                }
            }

            /*
             * Check if its valid
             * Flow:
                1. Change image[0][0] to flip
                2. Check
                3. Slowly flip all
                4. Slowly rotate all
             */

            //if (IsValid(image))
            //{
            //    Console.WriteLine("VALID 1!");
            //    Console.WriteLine(image[0][0].id * image[0][^1].id * image[^1][0].id * image[^1][^1].id);
            //    return;
            //}

            IEnumerable<IEnumerable<char>> possibleModes = GetPermutations("XRF", map.Count);
            Console.WriteLine(map.Count);
            IEnumerable<IEnumerable<int>> possiblePositions = GetPermutations(Enumerable.Range(0, map.Count), map.Count);
            Random rand = new Random();

            foreach (IEnumerable<char> combi in possibleModes)
            {
                List<char> combination = combi.ToList();
                //List<char> combination = new List<char>("XXXXXXXXX");
                //Console.WriteLine(string.Join("", combination));
                // 1. apply permutation
                Dictionary<int, Dictionary<int, Pixel>> toCheckImage = new Dictionary<int, Dictionary<int, Pixel>>();

                int c = 0;
                for (int i = 0; i < size; i++)
                {
                    toCheckImage[i] = new Dictionary<int, Pixel>();
                    for (int j = 0; j < size; j++)
                    {
                        image[i][j].Reset();
                        if (combination[c] == 'R')
                        {
                            image[i][j].Rotate();
                        }
                        else if (combination[c] == 'F')
                        {
                            image[i][j].Flip();
                        }
                        c++;
                    }
                }

                // randomly arrange as well

                //List<List<int>> possiblePositions = new List<List<int>>();
                //for (int i = 0; i < map.Count; i++)
                //{
                //    possiblePositions.Add(new List<int>());
                //    for (int j = 0; j < map.Count; j++)
                //    {
                //        possiblePositions[i].Add(j);
                //    }
                //}

                //while (possiblePositions[0].Count > 0) {
                //    //List<int> pos = new List<int>() { 0, 1, 2, 3, 4, 5, 6, 7,8};
                //    List<int> pos = new List<int>();

                //    foreach (List<int> i in possiblePositions) {
                //        int index = rand.Next(i.Count);
                //        pos.Add(i[index]);
                //        i.RemoveAt(index);
                //    }
                foreach (IEnumerable<int> perm in possiblePositions) {
                    List<int> pos = perm.ToList();
                    for (int cc = 0; cc < map.Count; cc++)
                    {
                        int row = (int)Math.Floor((decimal)(cc / size));
                        int column = cc % size;

                        int x = pos[cc];
                        int irow = (int)Math.Floor((decimal)(x / size));
                        int icolumn = x % size;
                        toCheckImage[row][column] = image[irow][icolumn];
                    }

                    if (IsValid(toCheckImage))
                    {
                        Console.WriteLine("VALID!");
                        Console.WriteLine(toCheckImage[0][0].id * toCheckImage[0][toCheckImage[0].Count - 1].id * toCheckImage[toCheckImage.Count - 1][0].id * toCheckImage[toCheckImage.Count - 1][toCheckImage[toCheckImage.Count - 1].Count - 1].id);
                        return;
                    }
                }
            }
        }

        static bool IsValid(Dictionary<int, Dictionary<int, Pixel>> image)
        {
            List<bool> checks = new List<bool>();
            for (int r = 0; r < image.Count; r++)
            {
                for (int c = 0; c < image[r].Count; c++)
                {
                    if (image[r].Count > c + 1 && c + 1 > 0)
                    {
                        checks.Add(image[r][c].GetRight() == image[r][c + 1].GetLeft());
                    }

                    if (image[r].Count > c - 1 && c - 1 > 0) {
                        checks.Add(image[r][c].GetLeft() == image[r][c - 1].GetRight());
                    }

                    if (image.Count > r - 1 && r - 1 > 0)
                    {
                        checks.Add(image[r][c].GetTop() == image[r - 1][c].GetBottom());
                    }

                    if (image.Count > r + 1 && r + 1 > 0)
                    {
                        checks.Add(image[r][c].GetBottom() == image[r + 1][c].GetTop());
                    }

                    if (checks.Any(x => x == false))
                    {
                        return false;
                    }
                    else
                    {
                        checks = new List<bool>();
                    }
                }
            }
            return true;
        }
        
        static IEnumerable<IEnumerable<T>> GetPermutations<T>(IEnumerable<T> list, int length)
        {
            if (length == 1)
            {
                return list.Select(t => new T[] { t });
            }

            return GetPermutations(list, length - 1).SelectMany(t => list, (t1, t2) => t1.Concat(new T[] { t2 }));
        }
    }
}
