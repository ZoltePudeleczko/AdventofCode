#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ifstream input("input.txt");
	vector<int> vec;
	vector<int> vec2;
	string tmp;
	while (getline(input, tmp))
	{
		vec.push_back(stoi(tmp));
		vec2.push_back(stoi(tmp));
	}

	int steps1 = 0;
	int pos = 0;
	while (pos >= 0 && pos < vec.size())
	{
		vec[pos]++;
		pos += vec[pos] - 1;
		steps1++;
	}

	int steps2 = 0;
	pos = 0;
	while (pos >= 0 && pos < vec2.size())
	{
		if (vec2[pos] >= 3)
		{
			vec2[pos]--;
			pos += vec2[pos] + 1;
		}
		else
		{
			vec2[pos]++;
			pos += vec2[pos] - 1;
		}
		steps2++;
	}

	cout << "Part I: " << steps1 << endl << "Part II: " << steps2 << endl;
	return 0;
}