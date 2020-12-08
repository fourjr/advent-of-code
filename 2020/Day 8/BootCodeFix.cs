using System;
using System.Collections.Generic;
using System.Reflection;

namespace Day_8
{
    public class BootCodeFix : BootCode
    {
        private bool triedChange;
        private List<int> triedChanging;

        public BootCodeFix(string[] _instructions) : base(_instructions) { }

        public int Fix()
        {
            triedChanging = new List<int>();

            while (true)
            {
                HashSet<int> instructionsRan = new HashSet<int>();
                triedChange = false;
                accumulator = 0;
                cursor = 0;
                while (cursor < instructions.Count)
                {
                    (InstructionType instruction, int value) = instructions[cursor];

                    object[] parameters = new object[] { value };
                    MethodInfo method = GetType().GetMethod($"Run{instruction}", BindingFlags.NonPublic | BindingFlags.Instance);
                    method.Invoke(this, parameters);

                    if (cursor == instructions.Count - 1)
                    {
                        return accumulator;
                    }

                    if (instructionsRan.Contains(cursor))
                    {
                        break;
                    }
                    else
                    {
                        instructionsRan.Add(cursor);
                    }
                    cursor++;
                }
            }

            throw new Exception("Invalid Boot Code, not an infinite loop.");
        }

        protected override void RunJMP(int value)
        {
            if (!triedChange && !triedChanging.Contains(cursor))
            {
                triedChange = true;
                triedChanging.Add(cursor);
                RunNOP(value);
            }
            else
            {
                base.RunJMP(value);
            }
        }

        protected override void RunNOP(int value)
        {
            if (!triedChange && !triedChanging.Contains(cursor))
            {
                triedChange = true;
                triedChanging.Add(cursor);
                RunJMP(value);
            }
            else
            {
                base.RunNOP(value);
            }
        }
    }
}