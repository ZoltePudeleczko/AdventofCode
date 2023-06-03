#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int ij2w(int i, int j);

int main()
{
	ifstream input("input.txt");
	int n, a;
	input >> n;
	
	/*Part One*/
	for (int i = 1;; i += 2)
	{
		a = i;
		if (a*a >= n)
			break;
	}
	int start = a*a;
	int i = 0; //row
	while (a > 1)
	{
		a -= 2;
		i++;
	}
	int j = i; //column
	int max = i;

	while (start != n)
	{
		if (j > -max && i == max)
			j--;
		else if (j == -max && i > -max)
			i--;
		else if (j < max && i == -max)
			j++;
		else if (j == max)
			i++;
		start--;
	}
	int steps = abs(i) + abs(j);

	/*Part Two*/
	int val;
	vector<int> tab;
	tab.push_back(1);
	i = 0; //row
	j = 0; //column
	max = 0;

	while (true)
	{
		if (i == max && j == max)
		{
			max++;
			j++;
		}
		else if (j == max && i > -max)
			i--;
		else if (i == -max && j > -max)
			j--;
		else if (j == -max && i < max)
			i++;
		else if (i == max && j < max)
			j++;

		val = 0;
		cout << i << " " << j << endl;
		if (ij2w(i - 1, j - 1) < tab.size())
			val += tab[ij2w(i - 1, j - 1)];
		if (ij2w(i - 1, j) < tab.size())
			val += tab[ij2w(i - 1, j)];
		if (ij2w(i, j - 1) < tab.size())
			val += tab[ij2w(i, j - 1)];
		if (ij2w(i + 1, j + 1) < tab.size())
			val += tab[ij2w(i + 1, j + 1)];
		if (ij2w(i + 1, j) < tab.size())
			val += tab[ij2w(i + 1, j)];
		if (ij2w(i, j + 1) < tab.size())
			val += tab[ij2w(i, j + 1)];
		if (ij2w(i - 1, j + 1) < tab.size())
			val += tab[ij2w(i - 1, j + 1)];
		if (ij2w(i + 1, j - 1) < tab.size())
			val += tab[ij2w(i + 1, j - 1)];

		if (val > n)
			break;
		tab.push_back(val);
	}

	cout << "Part I: " << steps << endl << "Part II: " << val;
}

int ij2w(int i, int j)
{
	if (i == 0 && j == 0)
		return 0;
	int ii = 0;
	int jj = 0;
	int max = 0;
	int ind = 0;
	while (true)
	{
		if (ii == max && jj == max)
		{
			max++;
			jj++;
		}
		else if (jj == max && ii > -max)
			ii--;
		else if (ii == -max && jj > -max)
			jj--;
		else if (jj == -max && ii < max)
			ii++;
		else if (ii == max && jj < max)
			jj++;
		ind++;
		if (ii == i && jj == j)
			return ind;
	}
}