using System;
using System.Collections.Generic;
using System.Linq;

namespace Day_16
{
    class Program
    {
        static Dictionary<string, List<int>> allRules = new Dictionary<string, List<int>>();

        static void Main()
        {
            string input = System.IO.File.ReadAllText("../../../input.txt");
            // Shared preprocessing
            string[] parts = input.Split("\r\n\r\n");
            string[] rules = parts[0].Split("\r\n");

            foreach (string line in rules)
            {
                string[] values = line.Split(": ");
                string name = values[0];
                List<int> validNumbers = new List<int>();
                foreach (string numbers in values[1].Split(" or "))
                {
                    string[] nums = numbers.Split("-");
                    for (int i = int.Parse(nums[0]); i <= int.Parse(nums[1]); i++)
                    {
                        validNumbers.Add(i);
                    }
                }

                allRules[name] = validNumbers;
            }

            Console.WriteLine(Part1(parts));
            Console.WriteLine(Part2(parts));
        }

        static int Part1(string[] parts) {
            IEnumerable<string> nearbyTickets = parts[2].Split("\r\n").Skip(1);

            int errorRate = 0;
            foreach (string line in nearbyTickets)
            {
                string[] lineSplit = line.Split(",");
                for (int i = 0; i < lineSplit.Length; i++)
                {
                    List<string> found = new List<string>();
                    int realNum = int.Parse(lineSplit[i]);
                    foreach (KeyValuePair<string, List<int>> rule in allRules)
                    {
                        if (rule.Value.Contains(realNum))
                        {
                            found.Add(rule.Key);
                        }
                    }
                    if (found.Count == 0)
                    {
                        errorRate += realNum;
                    }
                }
            }
            
            return errorRate;
        }

        static long Part2(string[] parts)
        {
            IEnumerable<string> nearbyTickets = parts[2].Split("\r\n").Skip(1);
            Dictionary<int, List<string>> allValues = new Dictionary<int, List<string>>();
            int validTickets = nearbyTickets.Count();

            foreach (string line in nearbyTickets)
            {
                bool ruined = false;
                Dictionary<int, List<string>> currValue = new Dictionary<int, List<string>>();
                string[] lineSplit = line.Split(",");
                for (int i = 0; i < lineSplit.Length; i++)
                {
                    List<string> found = new List<string>();
                    int realNum = int.Parse(lineSplit[i]);
                    foreach (KeyValuePair<string, List<int>> rule in allRules)
                    {
                        if (rule.Value.Contains(realNum))
                        {
                            found.Add(rule.Key);
                        }
                    }
                    if (found.Count == 0)
                    {
                        ruined = true;
                        validTickets--;
                        break;
                    }
                    else
                    {
                        if (currValue.ContainsKey(i))
                        {
                            currValue[i].AddRange(found);
                        }
                        else
                        {
                            currValue[i] = found;
                        }
                    }
                }

                if (!ruined)
                {
                    foreach (KeyValuePair<int, List<string>> r in currValue)
                    {

                        if (allValues.ContainsKey(r.Key))
                        {
                            allValues[r.Key].AddRange(r.Value);
                        }
                        else
                        {
                            allValues[r.Key] = r.Value;
                        }
                    }
                }
            }

            Dictionary<int, List<string>> possibleNames = new Dictionary<int, List<string>>();
            foreach (KeyValuePair<int, List<string>> rule in allValues)
            {
                int highestValue = 0;
                List<string> ruleName = new List<string>();
                HashSet<string> hash = new HashSet<string>(rule.Value);
                foreach (string r in hash)
                {
                    int count = rule.Value.Count(s => s == r);
                    if (count == validTickets)
                    {
                        highestValue = count;
                        ruleName.Add(r);
                    }
                }
                possibleNames[rule.Key] = ruleName;
            }

            List<KeyValuePair<int, List<string>>> sortedPossibleNames = possibleNames.ToList();

            sortedPossibleNames.Sort((pair1, pair2) => pair1.Value.Count.CompareTo(pair2.Value.Count));
            Dictionary<int, string> finalIndex = new Dictionary<int, string>();

            List<string> availableNames = new List<string>(allRules.Keys);
            foreach (KeyValuePair<int, List<string>> val in sortedPossibleNames)
            {
                string finalName = "";
                foreach (string name in val.Value)
                {
                    if (availableNames.Contains(name))
                    {
                        finalName = name;
                        availableNames.Remove(name);
                        break;
                    }
                }
                finalIndex[val.Key] = finalName;
            }

            long answer = 1;

            string myTicket = parts[1].Split("\r\n")[1];
            string[] myTicketSplit = myTicket.Split(",");
            for (int i = 0; i < myTicketSplit.Length; i++)
            {
                if (finalIndex[i].Contains("departure"))
                {
                    answer *= long.Parse(myTicketSplit[i]);
                }
            }

            return answer;
        }
    }
}
