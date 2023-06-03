#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <list>

using namespace std;

struct command {
	string name;
	char reg1;
	bool usesValue;
	int value;
	char reg2;
};

int main()
{
	ifstream input("input.txt");
	map<char, long long> registers = { {'a', 0}, { 'b', 0 }, { 'c', 0 }, { 'd', 0 }, { 'e', 0 }, { 'f', 0 }, { 'g', 0 }, { 'h', 0 }, { '1', 1} };
	vector<command> commands;
	string tmp;
	while (getline(input, tmp))
	{
		command t;
		t.name = tmp.substr(0, tmp.find(' '));
		t.reg1 = tmp[4];
		if (tmp.size() > 5)
		{
			if ((int)tmp[6] > 96 && (int)tmp[6] < 123)
			{
				t.usesValue = false;
				t.reg2 = tmp[6];
			}
			else
			{
				t.usesValue = true;
				t.value = stoi(tmp.substr(6));
			}
		}
		commands.push_back(t);
	}

	/* Part One */
	int pos = 0;
	int mulTimes = 0;
	while (pos >= 0 && pos < commands.size())
	{
		if (commands[pos].name == "mul")
			mulTimes++;

		if (commands[pos].name == "set")
			if (commands[pos].usesValue)
				registers[commands[pos].reg1] = commands[pos].value;
			else
				registers[commands[pos].reg1] = registers[commands[pos].reg2];
		else if (commands[pos].name == "sub")
			if (commands[pos].usesValue)
				registers[commands[pos].reg1] -= commands[pos].value;
			else
				registers[commands[pos].reg1] -= registers[commands[pos].reg2];
		else if (commands[pos].name == "mul")
			if (commands[pos].usesValue)
				registers[commands[pos].reg1] *= commands[pos].value;
			else
				registers[commands[pos].reg1] *= registers[commands[pos].reg2];

		if (commands[pos].name == "jnz" && registers[commands[pos].reg1] != 0)
			if (commands[pos].usesValue)
				pos += commands[pos].value;
			else
				pos += registers[commands[pos].reg2];
		else
			pos++;
	}
	cout << "Part I: " << mulTimes << endl;
	return 0;
}