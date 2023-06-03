using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advent_2018
{
    class Day1
    {
        static public int Day1Part1()
        {
            StreamReader sr = new StreamReader(Program.filesPath + @"\day1.txt");
            int frequency = 0;
            while (!sr.EndOfStream)
                frequency += int.Parse(sr.ReadLine());
            return frequency;
        }

        static public int Day1Part2()
        {
            StreamReader sr = new StreamReader(Program.filesPath + @"\day1.txt");
            int frequency = 0;
            List<int> reachedFrequences = new List<int>();
            while (!reachedFrequences.Contains(frequency))
            {
                reachedFrequences.Add(frequency);
                frequency += int.Parse(sr.ReadLine());
                if (sr.EndOfStream)
                    sr = new StreamReader(Program.filesPath + @"\day1.txt");
            }
            return frequency;
        }
    }
}