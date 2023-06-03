#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct danceMove {
	char name;
	int spin;
	int t1, t2;
	char tc1, tc2;
};

void justDance(danceMove dm, string &programs);

int main()
{
	ifstream input("input.txt");
	string programs = "abcdefghijklmnop";
	vector<danceMove> danceMoves;
	char a;
	int t1, t2;
	char tc1, tc2;
	while (!input.eof())
	{
		danceMove tmp;
		input.get(a);
		tmp.name = a;
		if (a == 's')
		{
			input.get(a);
			t1 = (int)a - 48;
			input.get(a);
			if (isalnum(a))
			{
				t1 = t1 * 10 + (int)a - 48;
				input.get(a);
			}
			tmp.spin = t1;
		}
		else if (a == 'x')
		{
			input.get(a);
			t1 = (int)a - 48;
			input.get(a);
			if (isalnum(a))
			{
				t1 = t1 * 10 + (int)a - 48;
				input.get(a);
			}
			input.get(a);
			t2 = (int)a - 48;
			input.get(a);
			if (isalnum(a))
			{
				t2 = t2 * 10 + (int)a - 48;
				input.get(a);
			}
			tmp.t1 = t1;
			tmp.t2 = t2;
		}
		else if (a == 'p')
		{
			input.get(tc1);
			input.get(a);
			input.get(tc2);
			input.get(a);
			tmp.tc1 = tc1;
			tmp.tc2 = tc2;
		}
		danceMoves.push_back(tmp);
	}
	vector<string> positions;
	positions.push_back(programs);
	bool loop = false;
	int loopSize;
	for (int i = 0; i < 1000000000; i++)
	{
		for (int j = 0; j < danceMoves.size(); j++)
			justDance(danceMoves[j], programs);
		for (int j = 0; j < positions.size(); j++)
		{
			if (programs == positions[j])
			{
				loop = true;
				loopSize = positions.size();
				break;
			}
		}
		if (loop)
			break;
		positions.push_back(programs);
		if (i == 0)
			cout << "Part I: " << programs << endl;
	}
	int pos = positions.size() - 1;
	if (loop)
		pos = 1000000000 % loopSize;
	cout << "Part II: " << positions[pos] << endl;
	return 0;
}

void justDance(danceMove dm, string &programs)
{
	if (dm.name == 's')
	{
		for (int k = 0; k < dm.spin; k++)
		{
			programs.insert(programs.begin(), programs[programs.size() - 1]);
			programs.pop_back();
		}
	}
	else if (dm.name == 'x')
	{
		swap(programs[dm.t1], programs[dm.t2]);
	}
	else if (dm.name == 'p')
	{
		for (int k = 0; k < programs.size(); k++)
		{
			if (programs[k] == dm.tc1)
				programs[k] = dm.tc2;
			else if (programs[k] == dm.tc2)
				programs[k] = dm.tc1;
		}
	}
}