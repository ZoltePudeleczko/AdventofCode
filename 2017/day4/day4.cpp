#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ifstream input("input.txt");
	string s;
	vector<string> vec, vec2;
	int pos, foundPos;
	bool isK, isK2;

	int sum1 = 0;
	int sum2 = 0;
	while (getline(input, s))
	{
		vec.resize(0);
		vec2.resize(0);
		pos = 0;
		while ((foundPos = s.find(' ', pos)) != string::npos)
		{
			vec.push_back(s.substr(pos, foundPos - pos));
			vec2.push_back(s.substr(pos, foundPos - pos));
			pos = foundPos + 1;
		}
		vec.push_back(s.substr(pos));
		vec2.push_back(s.substr(pos));
		for (int i = 0; i < vec2.size(); i++)
			sort(vec2[i].begin(), vec2[i].end());
		isK = true;
		isK2 = true;
		for (int i = 0; i < vec.size(); i++)
		{
			for (int j = i + 1; j < vec.size(); j++)
			{
				if (vec[i] == vec[j])
					isK = false;
				if (vec2[i] == vec2[j])
					isK2 = false;
			}
			if (!isK && !isK2)
				break;
		}
		if (isK)
			sum1++;
		if (isK2)
			sum2++;
	}

	cout << "Part I: " << sum1 << endl << "Part II: " << sum2 << endl;
	return 0;
}