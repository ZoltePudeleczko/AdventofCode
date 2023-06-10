#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <list>
#include <queue>

using namespace std;

struct command
{
	string name;
	char reg1;
	bool usesValue;
	long long value;
	char reg2;
};

int main()
{
	ifstream input("input.txt");
	map<char, long long> tmpRegisters;
	vector<command> commands;
	string tmp;
	while (getline(input, tmp))
	{
		command t;
		t.name = tmp.substr(0, tmp.find(' '));

		if (t.name == "snd" || t.name == "rcv")
		{
			if ((int)tmp[4] > 96 && (int)tmp[4] < 123)
			{
				t.usesValue = false;
				t.reg1 = tmp[4];
				if (tmpRegisters.find(t.reg1) == tmpRegisters.end())
					tmpRegisters[t.reg1] = 0;
			}
			else
			{
				t.usesValue = true;
				t.value = stoi(tmp.substr(4));
			}
		}
		else
		{
			t.reg1 = tmp[4];
			if (tmpRegisters.find(t.reg1) == tmpRegisters.end())
			{
				if ((int)t.reg1 > 96 && (int)t.reg1 < 123)
				{
					tmpRegisters[t.reg1] = 0;
				}
				else
					tmpRegisters[t.reg1] = 1;
			}
			if (tmp.size() > 5)
			{
				if ((int)tmp[6] > 96 && (int)tmp[6] < 123)
				{
					t.usesValue = false;
					t.reg2 = tmp[6];
					if (tmpRegisters.find(t.reg2) == tmpRegisters.end())
						tmpRegisters[t.reg2] = 0;
				}
				else
				{
					t.usesValue = true;
					t.value = stoi(tmp.substr(6));
				}
			}
		}

		commands.push_back(t);
	}

	/* Part One */
	map<char, long long> registers(tmpRegisters);

	int pos = 0;
	int soundPlaying = 0;
	while (pos >= 0 && pos < commands.size())
	{
		if (commands[pos].name == "snd")
			if (commands[pos].usesValue)
				soundPlaying = commands[pos].value;
			else
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
		else if (commands[pos].name == "rcv")
			if (commands[pos].usesValue && commands[pos].value != 0)
				break;
			else if (registers[commands[pos].reg1] != 0)
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

	/* Part Two */
	map<char, long long> firstRegisters(tmpRegisters);
	map<char, long long> secondRegisters(tmpRegisters);

	for (const auto &pair : secondRegisters)
	{
		secondRegisters[pair.first] = 1;
	}

	for (const auto &pair : secondRegisters)
	{
		cout << pair.first << " " << pair.second << endl;
	}

	int firstPosition = 0;
	int secondPosition = 0;
	bool firstAwaiting = false;
	bool secondAwaiting = false;
	queue<long long> firstQueue;
	queue<long long> secondQueue;

	int secondSendValues = 0;
	while (!firstAwaiting || !secondAwaiting || firstQueue.size() > 0 || secondQueue.size() > 0)
	{
		// Program 0
		if (commands[firstPosition].name == "snd")
			if (commands[firstPosition].usesValue)
				secondQueue.push(commands[firstPosition].value);
			else
				secondQueue.push(firstRegisters[commands[firstPosition].reg1]);
		else if (commands[firstPosition].name == "set")
			if (commands[firstPosition].usesValue)
				firstRegisters[commands[firstPosition].reg1] = commands[firstPosition].value;
			else
				firstRegisters[commands[firstPosition].reg1] = firstRegisters[commands[firstPosition].reg2];
		else if (commands[firstPosition].name == "add")
			if (commands[firstPosition].usesValue)
				firstRegisters[commands[firstPosition].reg1] += commands[firstPosition].value;
			else
				firstRegisters[commands[firstPosition].reg1] += firstRegisters[commands[firstPosition].reg2];
		else if (commands[firstPosition].name == "mul")
			if (commands[firstPosition].usesValue)
				firstRegisters[commands[firstPosition].reg1] *= commands[firstPosition].value;
			else
				firstRegisters[commands[firstPosition].reg1] *= firstRegisters[commands[firstPosition].reg2];
		else if (commands[firstPosition].name == "mod")
			if (commands[firstPosition].usesValue)
				firstRegisters[commands[firstPosition].reg1] %= commands[firstPosition].value;
			else
				firstRegisters[commands[firstPosition].reg1] %= firstRegisters[commands[firstPosition].reg2];
		else if (commands[firstPosition].name == "rcv")
			if (firstQueue.size() > 0)
			{
				firstRegisters[commands[firstPosition].reg1] = firstQueue.front();
				firstQueue.pop();
				firstAwaiting = false;
			}
			else
				firstAwaiting = true;

		if (commands[firstPosition].name == "jgz" && firstRegisters[commands[firstPosition].reg1] > 0)
			if (commands[firstPosition].usesValue)
				firstPosition += commands[firstPosition].value;
			else
				firstPosition += firstRegisters[commands[firstPosition].reg2];
		else if (!firstAwaiting)
			firstPosition++;

		// Program 1
		if (commands[secondPosition].name == "snd")
		{
			secondSendValues++;

			if (commands[secondPosition].usesValue)
			{
				firstQueue.push(commands[secondPosition].value);
			}
			else
			{
				firstQueue.push(secondRegisters[commands[secondPosition].reg1]);
			}
		}
		else if (commands[secondPosition].name == "set")
			if (commands[secondPosition].usesValue)
				secondRegisters[commands[secondPosition].reg1] = commands[secondPosition].value;
			else
				secondRegisters[commands[secondPosition].reg1] = secondRegisters[commands[secondPosition].reg2];
		else if (commands[secondPosition].name == "add")
			if (commands[secondPosition].usesValue)
				secondRegisters[commands[secondPosition].reg1] += commands[secondPosition].value;
			else
				secondRegisters[commands[secondPosition].reg1] += secondRegisters[commands[secondPosition].reg2];
		else if (commands[secondPosition].name == "mul")
			if (commands[secondPosition].usesValue)
				secondRegisters[commands[secondPosition].reg1] *= commands[secondPosition].value;
			else
				secondRegisters[commands[secondPosition].reg1] *= secondRegisters[commands[secondPosition].reg2];
		else if (commands[secondPosition].name == "mod")
			if (commands[secondPosition].usesValue)
				secondRegisters[commands[secondPosition].reg1] %= commands[secondPosition].value;
			else
				secondRegisters[commands[secondPosition].reg1] %= secondRegisters[commands[secondPosition].reg2];
		else if (commands[secondPosition].name == "rcv")
			if (secondQueue.size() > 0)
			{
				secondRegisters[commands[secondPosition].reg1] = secondQueue.front();
				secondQueue.pop();
				secondAwaiting = false;
			}
			else
				secondAwaiting = true;

		if (commands[secondPosition].name == "jgz" && secondRegisters[commands[secondPosition].reg1] > 0)
			if (commands[secondPosition].usesValue)
				secondPosition += commands[secondPosition].value;
			else
				secondPosition += secondRegisters[commands[secondPosition].reg2];
		else if (!secondAwaiting)
			secondPosition++;
	}

	cout << "Part II: " << secondSendValues << endl;
}