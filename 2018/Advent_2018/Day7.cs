using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advent_2018
{
    class Day7
    {
        public enum StepState
        {
            ToBeDone, Working, Done, NotActive
        }

        static public string Day7Part1()
        {
            bool[,] stepsRequirements = new bool[26,26];
            StepState[] stepsState = new StepState[26];
            StreamReader sr = new StreamReader(Program.filesPath + @"\day7.txt");
            while(!sr.EndOfStream)
            {
                string t = sr.ReadLine();
                stepsState[(int)t[5] - (int)'A'] = stepsState[(int)t[36] - (int)'A'] = StepState.ToBeDone;
                stepsRequirements[(int)t[36] - (int)'A', (int)t[5] - (int)'A'] = true;
            }
            bool somethingToBeDone, cantBeDone;
            string result = "";
            do
            {
                somethingToBeDone = false;
                for (int i = 0; i < stepsState.Length; i++)
                {
                    if (stepsState[i] == StepState.ToBeDone)
                        somethingToBeDone = true;
                }
                if (somethingToBeDone)
                {
                    for (int i = 0; i < stepsRequirements.GetLength(0); i++)
                    {
                        if (stepsState[i] == StepState.ToBeDone)
                        {
                            cantBeDone = false;
                            for (int j = 0; j < stepsRequirements.GetLength(1); j++)
                            {
                                if (stepsRequirements[i, j] && stepsState[j] != StepState.Done)
                                {
                                    cantBeDone = true;
                                    break;
                                }
                            }
                            if (cantBeDone)
                                continue;
                            stepsState[i] = StepState.Done;
                            result += (char)(i + (int)'A');
                            break;
                        }
                    }
                }
            } while (somethingToBeDone);
            return result;
        }

        static public int Day7Part2()
        {
            bool[,] stepsRequirements = new bool[26, 26];
            StepState[] stepsState = new StepState[26];
            StreamReader sr = new StreamReader(Program.filesPath + @"\day7.txt");
            while (!sr.EndOfStream)
            {
                string t = sr.ReadLine();
                stepsState[(int)t[5] - (int)'A'] = stepsState[(int)t[36] - (int)'A'] = StepState.ToBeDone;
                stepsRequirements[(int)t[36] - (int)'A', (int)t[5] - (int)'A'] = true;
            }
            int[] workers = new int[5] { -1, -1, -1, -1, -1 };
            int[] workersSecondsLeft = new int[5];
            int second = 0;
            bool somethingToBeDone, cantBeDone;
            string result = "";
            do
            {
                for (int i = 0; i < workers.Length; i++)
                {
                    if (workers[i] != -1)
                    {
                        workersSecondsLeft[i]--;
                        if (workersSecondsLeft[i] == 0)
                        {
                            stepsState[workers[i]] = StepState.Done;
                            result += (char)(workers[i] + (int)'A');
                            workers[i] = -1;
                        }
                    }
                }
                somethingToBeDone = false;
                for (int i = 0; i < stepsState.Length; i++)
                {
                    if (stepsState[i] == StepState.ToBeDone || stepsState[i] == StepState.Working)
                        somethingToBeDone = true;
                }
                if (somethingToBeDone)
                {
                    for (int i = 0; i < workers.Length; i++)
                    {
                        if (workers[i] == -1)
                        {
                            for (int j = 0; j < stepsRequirements.GetLength(0); j++)
                            {
                                if (stepsState[j] == StepState.ToBeDone)
                                {
                                    cantBeDone = false;
                                    for (int k = 0; k < stepsRequirements.GetLength(1); k++)
                                    {
                                        if (stepsRequirements[j, k] && stepsState[k] != StepState.Done)
                                        {
                                            cantBeDone = true;
                                            break;
                                        }
                                    }
                                    if (cantBeDone)
                                        continue;
                                    stepsState[j] = StepState.Working;
                                    workers[i] = j;
                                    workersSecondsLeft[i] = 60 + j + 1;
                                    break;
                                }
                            }
                        }
                    }
                }
                second++;
            } while (somethingToBeDone);
            return second - 1;
        }
    }
}
