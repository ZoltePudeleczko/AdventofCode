using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advent_2018
{
    class Day5
    {
        static public int Day5Part1()
        {
            string polymer = File.ReadAllLines(Program.filesPath + @"\day5.txt").ToList()[0];
            List<string> unitPairs = new List<string>();
            for (int i = 'a'; i <= 'z'; i++)
            {
                unitPairs.Add("" + (char)i + char.ToUpper((char)i));
                unitPairs.Add("" + char.ToUpper((char)i) + (char)i);
            }
            bool changed;
            int lastLength;
            do
            {
                changed = false;
                lastLength = polymer.Length;
                polymer = string.Join("", polymer.Split(unitPairs.ToArray(), StringSplitOptions.None));
                if (polymer.Length < lastLength)
                    changed = true;
            } while (changed);
            return polymer.Length;
        }

        static public int Day5Part2()
        {
            string polymer = File.ReadAllLines(Program.filesPath + @"\day5.txt").ToList()[0];
            List<char> units = new List<char>();
            List<string> unitPairs = new List<string>();
            for (int i = 'a'; i <= 'z'; i++)
            {
                units.Add((char)i);
                unitPairs.Add("" + (char)i + char.ToUpper((char)i));
                unitPairs.Add("" + char.ToUpper((char)i) + (char)i);
            }
            bool changed;
            string polymerEdited;
            int lastLength, shortest = int.MaxValue;
            for (int i = 0; i < units.Count; i++)
            {
                polymerEdited = string.Join("", polymer.Split(char.ToLower(units[i]), char.ToUpper(units[i])));
                do
                {
                    changed = false;
                    lastLength = polymerEdited.Length;
                    polymerEdited = string.Join("", polymerEdited.Split(unitPairs.ToArray(), StringSplitOptions.None));
                    if (polymerEdited.Length < lastLength)
                        changed = true;
                } while (changed);
                if (polymerEdited.Length < shortest)
                    shortest = polymerEdited.Length;
            }
            return shortest;
        }
    }
}