using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advent_2018
{
    class Day4
    {
        static public int Day4Part1()
        {
            Dictionary<int, int[]> guards = Day4Common();
            int sleepyGuardId = guards.Keys.ToList()[0];
            foreach (KeyValuePair<int, int[]> guardData in guards)
            {
                if (guardData.Value[60] > guards[sleepyGuardId][60])
                    sleepyGuardId = guardData.Key;
            }
            int sleepyMinute = 0;
            for (int i = 1; i < 60; i++)
            {
                if (guards[sleepyGuardId][i] > guards[sleepyGuardId][sleepyMinute])
                    sleepyMinute = i;
            }
            return sleepyGuardId * sleepyMinute;
        }

        static public int Day4Part2()
        {
            Dictionary<int, int[]> guards = Day4Common();
            int sleepyGuardId = guards.Keys.ToList()[0];
            int sleepyMinute = 0;
            foreach (KeyValuePair<int, int[]> guardData in guards)
            {
                for (int i = 0; i < 60; i++)
                {
                    if (guardData.Value[i] > guards[sleepyGuardId][sleepyMinute])
                    {
                        sleepyGuardId = guardData.Key;
                        sleepyMinute = i;
                    }
                }
            }
            return sleepyGuardId * sleepyMinute;
        }

        static private Dictionary<int, int[]> Day4Common()
        {
            StreamReader sr = new StreamReader(Program.filesPath + @"\day4.txt");
            List<Info> infos = new List<Info>();
            while (!sr.EndOfStream)
            {
                infos.Add(new Info(sr.ReadLine()));
            }
            infos.Sort();
            Dictionary<int, int[]> guards = new Dictionary<int, int[]>();
            int currentGuard = 0;
            int fallAsleep = 0;
            for (int i = 0; i < infos.Count; i++)
            {
                switch (infos[i].InfoType)
                {
                    case InfoType.beginsShift:
                        currentGuard = infos[i].GuardId;
                        if (!guards.ContainsKey(currentGuard))
                            guards.Add(currentGuard, new int[61]);
                        break;
                    case InfoType.fallsAsleep:
                        fallAsleep = infos[i].Date.Minute;
                        break;
                    case InfoType.wakesUp:
                        for (int j = fallAsleep; j < infos[i].Date.Minute; j++)
                        {
                            guards[currentGuard][j]++;
                        }
                        guards[currentGuard][60] += infos[i].Date.Minute - fallAsleep;
                        break;
                }
            }
            return guards;
        }

        public enum InfoType
        {
            beginsShift, fallsAsleep, wakesUp
        }

        public class Info : IComparable<Info>
        {
            public DateTime Date { get; set; }
            public int GuardId { get; set; }
            public InfoType InfoType { get; set; }

            public Info(string s)
            {
                Date = new DateTime(int.Parse(s.Substring(1, 4)), int.Parse(s.Substring(6, 2)), int.Parse(s.Substring(9, 2)), int.Parse(s.Substring(12, 2)), int.Parse(s.Substring(15, 2)), 0);
                string type = s.Substring(19, 5);
                if (type == "Guard")
                {
                    InfoType = InfoType.beginsShift;
                    GuardId = int.Parse(s.Substring(26, 4));
                }
                else if (type == "wakes")
                    InfoType = InfoType.wakesUp;
                else if (type == "falls")
                    InfoType = InfoType.fallsAsleep;
            }

            public int CompareTo(Info other)
            {
                if (Date.CompareTo(other.Date) != 0)
                    return Date.CompareTo(other.Date);
                return 0;
            }
        }
    }
}
