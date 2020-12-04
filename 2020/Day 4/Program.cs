using System;
using System.Collections.Generic;

namespace Day4
{
    class Program
    {
        static void Main()
        {
            string input = System.IO.File.ReadAllText("C:/Users/jiarong/Documents/jr/adventofcode/2020/Day 4/input.txt");
            Console.WriteLine(Part1(input));
            Console.WriteLine(Part2(input));
        }

        static int Part1(string input)
        {
            string[] inputSplit = input.Split("\r\n\r\n", StringSplitOptions.None);
            List<string> allFields = new List<string>() { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };
            int count = 0;

            foreach (string passport in inputSplit)
            {
                string[] fields = passport.Split(new Char[] { ' ', '\n' });
                List<string> keys = new List<string>();
                foreach (string f in fields)
                {
                    string[] kv = f.Split(":");
                    keys.Add(kv[0]);
                }
                int n = 0;
                foreach (string k in allFields)
                {
                    if (keys.Contains(k))
                    {
                        n++;
                    }
                }
                if (n == allFields.Count)
                {
                    count++;
                }
            }
            return count;            
        }

        static int Part2(string input)
        {
            string[] inputSplit = input.Split("\r\n\r\n", StringSplitOptions.None);
            List<string> allFields = new List<string>() { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };
            int count = 0;

            foreach (string passport in inputSplit)
            {
                string[] delim = { " ", "\r\n" };
                string[] fields = passport.Split(delim, StringSplitOptions.RemoveEmptyEntries);
                Dictionary<string, string> allVals = new Dictionary<string, string>();
                foreach (string f in fields)
                {
                    string[] kv = f.Split(":");
                    allVals.Add(kv[0], kv[1]);
                }
                int n = 0;
                int nn = 0;
                foreach (string k in allFields)
                {
                    if (allVals.ContainsKey(k))
                    {
                        string value = allVals[k];
                        bool isNumeric = int.TryParse(value, out _);
                        switch (k)
                        {
                            case "byr":
                                if (isNumeric && value.Length == 4 && int.Parse(value) >= 1920 && int.Parse(value) <= 2002)
                                {
                                    n++;
                                }
                                break;
                            case "iyr":
                                if (isNumeric && value.Length == 4 && int.Parse(value) >= 2010 && int.Parse(value) <= 2020)
                                {
                                    n++;
                                }
                                break;
                            case "eyr":
                                if (isNumeric && value.Length == 4 && int.Parse(value) >= 2020 && int.Parse(value) <= 2030)
                                {
                                    n++;
                                }
                                break;
                            case "hgt":
                                if (value.Length - 2 > 0)
                                {
                                    string num = value.Substring(0, value.Length - 2);
                                    string unit = value.Substring(value.Length - 2);
                                    bool numeric = int.TryParse(num, out _);
                                    if (unit == "cm")
                                    {
                                        if (numeric && int.Parse(num) >= 150 && int.Parse(num) <= 193)
                                        {
                                            n++;
                                        }
                                    }
                                    else if (unit == "in")
                                    {
                                        if (numeric && int.Parse(num) >= 59 && int.Parse(num) <= 76)
                                        {
                                            n++;
                                        }
                                    }
                                }
                                break;
                            case "hcl":
                                value = value.ToLower();
                                if (value.Length == 7 && value[0] == '#')
                                {
                                    int cn = 0;
                                    foreach (char c in value.Substring(1))
                                    {
                                        if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9' || c == 'a' || c == 'b' || c == 'c' || c == 'd' || c == 'e' || c == 'f')
                                        {
                                            cn++;
                                        }
                                    }
                                    if (cn == value.Length - 1)
                                    {
                                        n++;
                                    }
                                }
                                break;
                            case "ecl":
                                if (value == "amb" || value == "blu" || value == "brn" || value == "gry" || value == "grn" || value == "hzl" || value == "oth")
                                {
                                    n++;
                                }
                                break;
                            case "pid":
                                if (value.Length == 9 && isNumeric)
                                {
                                    n++;
                                }
                                break;
                        }
                    }
                    nn++;
                }
                if (n == allFields.Count)
                {
                    count++;
                }
            }
            return count;
        }
    }
}
