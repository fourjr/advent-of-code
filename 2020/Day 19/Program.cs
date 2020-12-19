using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

/*
 * I spent close to 13 hours on Day 19
 * Solved part 1, code is in pt1.txt, in about an hour
 * Pretty sure there is a stack overflow exception now though
 * but in no mood to refactor it/look at it again
 * 
 * I have not solved Part 2, no clue how/where I went wrong
 * Code is messy with no plans to refactor
 * Good night
*/

namespace Day_19
{
    public class Rule
    {
        public bool isList;
        public bool isAny;
        public int ruleNo;
        public List<Rule> listContent;
        public string stringContent;
        public int length
        {
            get
            {
                if (isList)
                {
                    if (isAny)
                    {
                        return listContent.Max(x => x.length);
                    }
                    else
                    {
                        return listContent.Sum(x => x.length);
                    }
                }
                else
                {
                    return stringContent.Length;
                }
            }
        }
        public Rule(List<Rule> l, int ruleNo, bool any = false)
        {
            listContent = l;
            isList = true;
            isAny = any;
        }
        public Rule(string s, int ruleNo, bool any = false)
        {
            stringContent = s;
            isList = false;
            isAny = any;
        }

        public override string ToString()
        {
            return $"Day_19.Rule-{ruleNo}-{isList}-{length}";
        }
    }
    class Program
    {
        static Dictionary<int, string> rules = new Dictionary<int, string>();

        static int GetLength(string rule)
        {
            List<string> realRule = new List<string>(rule.Split(' ').Skip(1));
            if (realRule.Count() == 1 && realRule[0].StartsWith('"') && realRule[0].EndsWith('"'))
            {
                // str
                return realRule[0].Trim('"').Length;
            }
            else
            {
                // not str
                List<int> lengths = new List<int>();
                int currL = 0;

                foreach (string x in realRule)
                {
                    if (x == "|")
                    {
                        break;
                    }
                    else
                    {
                        currL += GetLength(rules[int.Parse(x)]);
                    }
                }
                //if (currL > 0)
                //{
                //    lengths.Add(currL);
                //}
                //return lengths.Max();
                return currL;
            }
        }
        static bool ParseRule(string rule, string m, bool partTwo)
        {
            Console.WriteLine($"{rule}-{m}");
            List<string> realRule = new List<string>(rule.Split(' ').Skip(1));
            if (realRule.Count() == 1 && realRule[0].StartsWith('"') && realRule[0].EndsWith('"'))
            {
                // str
                if (m == realRule[0].Trim('"'))
                {
                    return true;
                }
                return false;
            }
            else
            {
                // not str
                int runIndex = 0;
                bool runMainLoop = true;
                while (runMainLoop)
                {
                    int i = 0;
                    List<bool> check = new List<bool>();
                    int count = 0;
                    foreach (string x in realRule)
                    {
                        //Console.WriteLine($"E: {x}");
                        int length = 0;
                        if (x == "|")
                        {
                            if (check.Count > 0 && check.All(x => x == true))
                            {
                                return true;
                            }
                            check = new List<bool>();
                            i = 0;
                        }
                        else
                        {
                            if (check.Any(x => x == false))
                            {
                                continue;
                            }

                            length = GetLength(rules[int.Parse(x)]);
                            List<int> possibleLengths = new List<int>();
                            while (true)
                            {
                                if (i + length > m.Length)
                                {
                                    if (runIndex >= possibleLengths.Count)
                                    {
                                        runMainLoop = false;
                                    }
                                    //Console.WriteLine($"A{m} - {i + length},{m.Length}");

                                    if (possibleLengths.Count > 0)
                                    {
                                        if (runMainLoop)
                                        {
                                            length = possibleLengths[runIndex];
                                        }
                                        check.Add(true);
                                    }
                                    else
                                    {
                                        check.Add(false);
                                    }
                                    break;
                                }
                                //Console.WriteLine(length);
                                bool c;

                                if (i + length < m.Length && count == realRule.Count - 1)
                                {
                                    //Console.WriteLine($"E{m} - {i + length},{m.Length}");
                                    c = false;
                                }
                                else
                                {
                                    //Console.WriteLine($"{x}-{rule}");
                                    c = ParseRule(rules[int.Parse(x)], m.Substring(i, length), partTwo);
                                }

                                if (c)
                                {
                                    possibleLengths.Add(length);
                                    //Console.WriteLine($"{rule} {x}: true");
                                }

                                if ((rule.StartsWith("8: ") || x == "8") && partTwo)
                                {
                                    length += GetLength(rules[8]);
                                }
                                else if ((rule.StartsWith("11: ") || x == "11") && partTwo)
                                {
                                    length += GetLength(rules[11]);
                                }
                                else
                                {
                                    check.Add(c);
                                    break;
                                }
                            }
                        }
                        i += length;
                        count++;
                    }

                    if (check.Count > 0)
                    {
                        if (check.All(x => x == true))
                        {
                            return true;
                        }
                    }
                    runIndex++;

                    if (!rule.StartsWith("8: ") && !rule.StartsWith("11: ") && realRule.All(x => x != "8" && x != "11"))
                    {
                        break;
                    }
                }
                return false;
            }
        }

        static bool IsValid(Rule r, string m)
        {
            //Console.WriteLine(r);
            if (r.isList)
            {
                List<bool> allValid = new List<bool>();
                int i = 0;
                foreach (Rule rule in r.listContent)
                {
                    if (r.isAny)
                    {
                        bool valid = IsValid(rule, m);
                        if (valid)
                        {
                            return true;
                        }
                    }
                    else
                    {
                        allValid.Add(IsValid(rule, m.Substring(i, rule.length).ToString()));
                    }
                    i += rule.length;
                }

                if (i < m.Length)
                {
                    return false;
                }

                if (!r.isAny)
                {
                    if (allValid.All(x => x == true))
                    {
                        return true;
                    }
                }
                return false;
            }
            else
            {
                //Console.WriteLine($"{r.stringContent} - {m}");
                return r.stringContent == m;
            }
        }
        static void Main()
        {
            bool partTwo = true;
            string input = System.IO.File.ReadAllText("../../../input.txt");
            string[] inputSplit = input.Split("\r\n\r\n");

            string[] rulesArr = inputSplit[0].Split("\r\n");

            foreach (string r in rulesArr)
            {
                int num = int.Parse(r.Split(' ')[0].Substring(0, r.Split(' ')[0].Length - 1));
                string updatedR;
                if (num == 8 && partTwo)
                {
                    updatedR = "8: 42 | 42 8";
                }
                else if (num == 11 && partTwo)
                {
                    updatedR = "11: 42 31 | 42 11 31";
                }
                else
                {
                    updatedR = r;
                }
                rules.Add(num, updatedR);
            }

            string[] messages = inputSplit[1].Split("\r\n");

            int count = 0;
            foreach (string m in messages) {
                bool validity = ParseRule(rules[0], m, partTwo);
                //Console.WriteLine($"{m}: {validity}");
                if (validity)
                {
                    Console.WriteLine(m);
                    count++;
                }
            }
            Console.WriteLine(count);
        }
    }
}
