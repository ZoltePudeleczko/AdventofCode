#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	ifstream input("input.txt");
	int a;
	vector<vector<int>> used;
	vector<int> act;
	while (!input.eof())
	{
		input >> a;
		act.push_back(a);
	}
	used.push_back(act);
	int maxPos, maxVal, actPos, usedPos, cycles = 0;
	bool isAlready = false;
	while (true)
	{
		cycles++;
		maxPos = 0;
		for (int i = 1; i < act.size(); i++)
			if (act[i] > act[maxPos]) maxPos = i;
		maxVal = act[maxPos];
		act[maxPos] = 0;
		actPos = (maxPos + 1) % act.size();
		for (int i = 0; i < maxVal; i++)
		{
			act[actPos]++;
			actPos = (actPos + 1) % act.size();
		}

		for (int i = 0; i < used.size(); i++)
		{
			if (used[i] == act)
			{
				isAlready = true;
				usedPos = i;
				break;
			}
		}
		
		if (isAlready)
			break;
		else
			used.push_back(act);
	}
	cout << "Part I: " << cycles << endl << "Part II: " << cycles - usedPos << endl;
	return 0;
}