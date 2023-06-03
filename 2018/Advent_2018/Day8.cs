using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advent_2018
{
    class Day8
    {
        static public int Day8Part1()
        {
            List<int> numbers = File.ReadAllLines(Program.filesPath + @"\day8.txt")[0].Split(' ').Select(x => int.Parse(x)).ToList();
            Node head = MakeTree(numbers);
            int metadataSum = Count1(head);
            return metadataSum;
        }

        static public int Day8Part2()
        {
            List<int> numbers = File.ReadAllLines(Program.filesPath + @"\day8.txt")[0].Split(' ').Select(x => int.Parse(x)).ToList();
            Node head = MakeTree(numbers);
            int metadataSum = Count2(head);
            return metadataSum;
        }

        static private int Count1(Node p)
        {
            int actSum = 0;
            for (int i = 0; i < p.Childs.Length; i++)
                actSum += Count1(p.Childs[i]);
            for (int i = 0; i < p.Metadata.Length; i++)
                actSum += p.Metadata[i];
            return actSum;
        }

        static private int Count2(Node p)
        {
            int actSum = 0;
            if (p.Childs.Length == 0)
            {
                for (int i = 0; i < p.Metadata.Length; i++)
                    actSum += p.Metadata[i];
            }
            else
            {
                for (int i = 0; i < p.Metadata.Length; i++)
                {
                    if (p.Metadata[i] != 0 && p.Metadata[i] <= p.Childs.Length)
                        actSum += Count2(p.Childs[p.Metadata[i] - 1]);
                }
            }
            return actSum;
        }

        static private Node MakeTree(List<int> numbers)
        {
            Node head = null;
            Node p = head;
            int i = 0;
            while (i < numbers.Count)
            {
                if (head == null)
                {
                    Node t = new Node(numbers[i], numbers[i + 1], p);
                    i += 2;
                    head = t;
                    p = head;
                    continue;
                }
                else
                {
                    bool goNext = false;
                    for (int j = 0; j < p.Childs.Length; j++)
                    {
                        if (p.Childs[j] == null)
                        {
                            Node t = new Node(numbers[i], numbers[i + 1], p);
                            i += 2;
                            p.Childs[j] = t;
                            p = p.Childs[j];
                            goNext = true;
                            break;
                        }
                    }
                    if (goNext)
                        continue;
                }
                for (int j = 0; j < p.Metadata.Length; j++)
                {
                    p.Metadata[j] = numbers[i];
                    i++;
                }
                p = p.Parent;
            }
            return head;
        }

        public class Node
        {
            public Node[] Childs { get; set; }
            public int[] Metadata { get; set; }
            public Node Parent { get; set; }

            public Node(int nchilds, int nmetadata, Node parent)
            {
                Childs = new Node[nchilds];
                Metadata = new int[nmetadata];
                Parent = parent;
            }
        }
    }
}
