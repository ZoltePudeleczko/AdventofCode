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
	map<char, long long> registers;
	vector<command> commands;
	string tmp;
	while (getline(input, tmp))
	{
		command t;
		t.name = tmp.substr(0, tmp.find(' '));
		t.reg1 = tmp[4];
		if (registers.find(t.reg1) == registers.end())
			registers[t.reg1] = 0;
		if (tmp.size() > 5)
		{
			if ((int)tmp[6] > 96 && (int)tmp[6] < 123)
			{
				t.usesValue = false;
				t.reg2 = tmp[6];
				if (registers.find(t.reg2) == registers.end())
					registers[t.reg2] = 0;
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
	int soundPlaying = 0;
	while (pos >= 0 && pos < commands.size())
	{
		if (commands[pos].name == "snd")
			soundPlaying = registers[commands[pos].reg1];
		else if (commands[pos].name == "set")
			if (commands[pos].usesValue)
				registers[commands[pos].reg1] = commands[pos].value;
			else
				registers[commands[pos].reg1] = registers[commands[pos].reg2];
		else if (commands[pos].name == "add")
			if (commands[pos].usesValue)
				registers[commands[pos].reg1] += commands[pos].value;
			else
				registers[commands[pos].reg1] += registers[commands[pos].reg2];
		else if (commands[pos].name == "mul")
			if (commands[pos].usesValue)
				registers[commands[pos].reg1] *= commands[pos].value;
			else
				registers[commands[pos].reg1] *= registers[commands[pos].reg2];
		else if (commands[pos].name == "mod")
			if (commands[pos].usesValue)
				registers[commands[pos].reg1] %= commands[pos].value;
			else
				registers[commands[pos].reg1] %= registers[commands[pos].reg2];
		else if (commands[pos].name == "rcv" && registers[commands[pos].reg1] != 0)
			break;

		if (commands[pos].name == "jgz" && registers[commands[pos].reg1] > 0)
			if (commands[pos].usesValue)
				pos += commands[pos].value;
			else
				pos += registers[commands[pos].reg2];
		else
			pos++;
	}
	cout << "Part I: " << soundPlaying << endl;
	return 0;
}