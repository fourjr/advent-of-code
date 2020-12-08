using System;
using System.Collections.Generic;
using System.Reflection;

namespace Day_8
{
    public class BootCode
    {
        protected int accumulator;
        protected int cursor;
        protected List<(InstructionType, int)> instructions = new List<(InstructionType, int)>();

        public BootCode(string[] _instructions)
        {
            for (int i = 0; i < _instructions.Length; i++)
            {
                string line = _instructions[i];
                string[] commands = line.Split(" ");
                Enum.TryParse(commands[0].ToUpper(), out InstructionType type);
                int number = int.Parse(commands[1]);

                instructions.Add((type, number));
            }
        }

        public virtual int Execute()
        {
            HashSet<int> instructionsRan = new HashSet<int>();
            accumulator = 0;
            cursor = 0;

            while (cursor < instructions.Count)
            {
                (InstructionType instruction, int value) = instructions[cursor];

                object[] parameters = new object[] { value };
                MethodInfo method = GetType().GetMethod($"Run{instruction}", BindingFlags.NonPublic | BindingFlags.Instance);
                method.Invoke(this, parameters);
                if (instructionsRan.Contains(cursor))
                {
                    return accumulator;
                }
                else
                {
                    instructionsRan.Add(cursor);
                }

                cursor++;
            }

            throw new Exception("Invalid Boot Code, not an infinite loop.");
        }

        protected virtual void RunACC(int value)
        {
            accumulator += value;
        }

        protected virtual void RunJMP(int value)
        {
            cursor += value - 1;
        }
        protected virtual void RunNOP(int value)
        { }
    }

    public enum InstructionType
    {
        ACC,
        JMP,
        NOP
    }
}