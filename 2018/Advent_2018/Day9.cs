using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advent_2018
{
    class Day9
    {
        public static long Day9Part1(int modifier = 1)
        {
            string input = new StreamReader(Program.filesPath + @"\day9.txt").ReadLine();
            long nPlayers = long.Parse(input.Substring(0, input.IndexOf(' ')));
            long maxMarble = long.Parse(input.Substring(input.IndexOf("worth") + 5, input.IndexOf("points") - input.IndexOf("worth") - 5)) * modifier;
            LinkedList<long> circle = new LinkedList<long>();
            circle.AddLast(0);
            LinkedListNode<long> curIndex = circle.Last;
            long[] points = new long[nPlayers];
            long curPlayer = 0;
            for (long nextMarble = 1; nextMarble <= maxMarble; nextMarble++)
            {
                if (nextMarble % 23 == 0)
                {
                    for (int i = 0; i < 7; i++)
                        curIndex = curIndex.Previous ?? circle.Last;
                    points[curPlayer] += (nextMarble + curIndex.Value);
                    LinkedListNode<long> tmp = curIndex;
                    curIndex = curIndex.Next ?? circle.First;
                    circle.Remove(tmp);
                }
                else
                {
                    curIndex = curIndex.Next ?? circle.First;
                    circle.AddAfter(curIndex, nextMarble);
                    curIndex = curIndex.Next ?? circle.First;
                }
                curPlayer++;
                if (curPlayer == nPlayers)
                    curPlayer = 0;
            }
            long max = 0;
            for (int i = 0; i < nPlayers; i++)
            {
                if (points[i] > max)
                    max = points[i];
            }
            return max;
        }

        public static long Day9Part2()
        {
            return Day9Part1(100);
        }
    }
}