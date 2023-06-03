using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advent_2018
{
    class Day6
    {
        static public int Day6Part1()
        {
            List<Point> destinations = new List<Point>();
            StreamReader sr = new StreamReader(Program.filesPath + @"\day6.txt");
            while (!sr.EndOfStream)
            {
                string t = sr.ReadLine();
                destinations.Add(new Point(int.Parse(t.Substring(0, t.IndexOf(','))), int.Parse(t.Substring(t.IndexOf(',') + 1))));
            }
            int xMax, yMax;
            xMax = yMax = 0;
            for (int i = 0; i < destinations.Count; i++)
            {
                if (destinations[i].X > xMax)
                    xMax = destinations[i].X;
                if (destinations[i].Y > yMax)
                    yMax = destinations[i].Y;
            }
            int minDistance, minDistanceDestination;
            int[,] area = new int[xMax, yMax];
            for (int i = 0; i < xMax; i++)
            {
                for (int j = 0; j < yMax; j++)
                {
                    minDistanceDestination = -1;
                    minDistance = int.MaxValue;
                    for (int k = 0; k < destinations.Count; k++)
                    {
                        int curDistance = Math.Abs(i - destinations[k].X) + Math.Abs(j - destinations[k].Y);
                        if (curDistance < minDistance)
                        {
                            minDistanceDestination = k;
                            minDistance = curDistance;
                        }
                        else if (curDistance == minDistance)
                        {
                            minDistanceDestination = -1;
                        }
                    }
                    area[i, j] = minDistanceDestination;
                }
            }
            int[] destinationsCount = new int[destinations.Count];
            for (int i = 0; i < xMax; i++)
            {
                for (int j = 0; j < yMax; j++)
                {
                    if (area[i, j] != -1)
                        destinationsCount[area[i, j]]++;
                }
            }
            for (int i = 0; i < xMax; i++)
            {
                if (area[i, 0] != -1)
                    destinationsCount[area[i, 0]] = -1;
                if (area[i, yMax - 1] != -1)
                    destinationsCount[area[i, yMax - 1]] = -1;
            }
            for (int j = 0; j < yMax; j++)
            {
                if (area[0, j] != -1)
                    destinationsCount[area[0, j]] = -1;
                if (area[xMax - 1, j] != -1)
                    destinationsCount[area[xMax - 1, j]] = -1;
            }
            int bestArea = 0;
            for (int i = 0; i < destinations.Count; i++)
            {
                if (destinationsCount[i] > bestArea)
                    bestArea = destinationsCount[i];
            }
            return bestArea;
        }

        static public int Day6Part2()
        {
            List<Point> destinations = new List<Point>();
            StreamReader sr = new StreamReader(Program.filesPath + @"\day6.txt");
            while (!sr.EndOfStream)
            {
                string t = sr.ReadLine();
                destinations.Add(new Point(int.Parse(t.Substring(0, t.IndexOf(','))), int.Parse(t.Substring(t.IndexOf(',') + 1))));
            }
            int xMax, yMax;
            xMax = yMax = 0;
            for (int i = 0; i < destinations.Count; i++)
            {
                if (destinations[i].X > xMax)
                    xMax = destinations[i].X;
                if (destinations[i].Y > yMax)
                    yMax = destinations[i].Y;
            }
            int curDistance, safeRegionSize = 0;
            int[,] area = new int[xMax, yMax];
            for (int i = 0; i < xMax; i++)
            {
                for (int j = 0; j < yMax; j++)
                {
                    curDistance = 0;
                    for (int k = 0; k < destinations.Count; k++)
                    {
                        curDistance += Math.Abs(i - destinations[k].X) + Math.Abs(j - destinations[k].Y);
                    }
                    if (curDistance < 10000)
                        safeRegionSize++;
                }
            }
            return safeRegionSize;
        }
    }
}
