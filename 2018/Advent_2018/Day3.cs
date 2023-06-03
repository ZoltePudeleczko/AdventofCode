using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advent_2018
{
    class Day3
    {
        static public int Day3Part1()
        {
            int[,] square = new int[1000, 1000];
            List<string> claims = File.ReadAllLines(Program.filesPath + @"\day3.txt").ToList();
            for (int i = 0; i < claims.Count; i++)
            {
                int xStart = int.Parse(claims[i].Substring(claims[i].IndexOf('@') + 1, claims[i].IndexOf(',') - claims[i].IndexOf('@') - 1));
                int yStart = int.Parse(claims[i].Substring(claims[i].IndexOf(',') + 1, claims[i].IndexOf(':') - claims[i].IndexOf(',') - 1));
                int xLength = int.Parse(claims[i].Substring(claims[i].IndexOf(':') + 1, claims[i].IndexOf('x') - claims[i].IndexOf(':') - 1));
                int yLength = int.Parse(claims[i].Substring(claims[i].IndexOf('x') + 1));
                for (int x = xStart; x < xStart + xLength; x++)
                {
                    for (int y = yStart; y < yStart + yLength; y++)
                    {
                        if (square[x, y] == 0)
                            square[x, y] = 1;
                        else if (square[x, y] == 1)
                            square[x, y] = 2;
                    }
                }
            }
            int overlap = 0;
            for (int i = 0; i < square.GetLength(0); i++)
            {
                for (int j = 0; j < square.GetLength(1); j++)
                {
                    if (square[i, j] == 2)
                        overlap++;
                }
            }
            return overlap;
        }

        internal static object Day3Part2()
        {
            int[,] square = new int[1000, 1000];
            List<string> claims = File.ReadAllLines(Program.filesPath + @"\day3.txt").ToList();
            List<int> intactClaims = new List<int>();
            for (int i = 0; i < claims.Count; i++)
            {
                int id = int.Parse(claims[i].Substring(claims[i].IndexOf('#') + 1, claims[i].IndexOf('@') - claims[i].IndexOf('#') - 1));
                int xStart = int.Parse(claims[i].Substring(claims[i].IndexOf('@') + 1, claims[i].IndexOf(',') - claims[i].IndexOf('@') - 1));
                int yStart = int.Parse(claims[i].Substring(claims[i].IndexOf(',') + 1, claims[i].IndexOf(':') - claims[i].IndexOf(',') - 1));
                int xLength = int.Parse(claims[i].Substring(claims[i].IndexOf(':') + 1, claims[i].IndexOf('x') - claims[i].IndexOf(':') - 1));
                int yLength = int.Parse(claims[i].Substring(claims[i].IndexOf('x') + 1));
                bool intact = true;
                for (int x = xStart; x < xStart + xLength; x++)
                {
                    for (int y = yStart; y < yStart + yLength; y++)
                    {
                        if (square[x, y] == 0)
                            square[x, y] = id;
                        else
                        {
                            intact = false;
                            if (intactClaims.Contains(square[x, y]))
                                intactClaims.Remove(square[x, y]);
                        }
                    }
                }
                if (intact)
                    intactClaims.Add(id);
            }
            return intactClaims[0];
        }
    }
}
