using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advent_2018
{
    class Day2
    {
        static public int Day2Part1()
        {
            StreamReader sr = new StreamReader(Program.filesPath + @"\day2.txt");
            int twoTimes = 0;
            int threeTimes = 0;
            bool two, three;
            string word;
            while (!sr.EndOfStream)
            {
                two = three = false;
                word = sr.ReadLine();
                for (int i = 0; i < word.Length; i++)
                {
                    int count = word.Count(x => x == word[i]);
                    if (count == 2)
                        two = true;
                    if (count == 3)
                        three = true;
                }
                if (two)
                    twoTimes++;
                if (three)
                    threeTimes++;
            }
            return twoTimes * threeTimes;
        }

        static public string Day2Part2()
        {
            List<string> words = File.ReadAllLines(Program.filesPath + @"\day2.txt").ToList();
            for (int i = 0; i < words.Count - 1; i++)
            {
                for (int j = i + 1; j < words.Count; j++)
                {
                    string result = "";
                    for (int k = 0; k < words[i].Length; k++)
                    {
                        if (words[i][k] == words[j][k])
                        {
                            result += words[i][k];
                        }
                        if (result.Length == words[i].Length - 1)
                            return result;
                    }
                }
            }
            return "";
        }
    }
}
