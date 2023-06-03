#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	ifstream input("input.txt");
	string s;
	vector<int> vec;
	int act, min, max, pos, foundPos;
	int sum1 = 0;
	int sum2 = 0;
	while (getline(input, s))
	{
		vec.resize(0);
		pos = 0;
		while ((foundPos = s.find('\t', pos)) != string::npos)
		{
			vec.push_back(stoi(s.substr(pos, foundPos - pos)));
			pos = foundPos + 1;
		}
		vec.push_back(stoi(s.substr(pos)));
		min = max = vec[0];
		for (int i = 0; i < vec.size(); i++)
		{
			for (int j = 0; j < vec.size(); j++)
			{
				if (i == j)
					continue;
				if (vec[i] % vec[j] == 0)
					sum2 += (vec[i] / vec[j]);
			}
			if (vec[i] > max)
				max = vec[i];
			if (vec[i] < min)
				min = vec[i];
		}
		sum1 += (max - min);
	}
	cout << "Checksum: " << sum1 << endl << "Sum of each row's result: " << sum2 << endl;
	return 0;
}