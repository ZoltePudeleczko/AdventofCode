#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <list>

using namespace std;

struct command
{
	string name;
	char reg1;
	bool usesValue;
	int value;
	char reg2;
};

int main()
{
	ifstream input("input.txt");
	map<char, long long> registers = {{'a', 0}, {'b', 0}, {'c', 0}, {'d', 0}, {'e', 0}, {'f', 0}, {'g', 0}, {'h', 0}, {'1', 1}};
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

	/* Part Two */
	// Let's use the power of our brains and analize what is going on really in the algorithm when a is 1
	// input_analyzed.txt gives some insight
	// We can see that the algorithm is trying to find the number of non-primes between 108100 and 125100 (inclusive) with a step of 17
	// So we can just count them and we will have the answer

	int startingNumber = 108100;
	int endNumber = 125100;

	int nonPrimes = 0;
	int number = startingNumber;
	do
	{
		bool isNotPrime = false;
		for (int i = 2; i <= number / 2; i++)
		{
			if (number % i == 0)
			{
				isNotPrime = true;
				break;
			}
		}

		if (isNotPrime)
		{
			nonPrimes++;
		}

		number += 17;
	} while (number <= endNumber);

	cout << "Part II: " << nonPrimes << endl;
}