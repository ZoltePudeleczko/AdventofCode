#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main()
{
	ifstream input("input.txt");
	map<string, int> registers;
	string tmp, in1, in2, instruction, operation;

	int pos, pos2, increaseValue, operationValue;

	int max2 = 0;
	while (getline(input, tmp))
	{
		pos = tmp.find(' ');
		in1 = tmp.substr(0, pos);
		instruction = tmp.substr(pos + 1, 3);
		increaseValue = stoi(tmp.substr(pos + 5));
		pos = tmp.find("if", pos);
		pos2 = tmp.find(' ', pos + 3);
		in2 = tmp.substr(pos + 3, pos2 - pos - 3);
		operation = tmp.substr(pos2 + 1, 2);
		operationValue = stoi(tmp.substr(pos2 + 3));

		if (registers.find(in1) == registers.end())
			registers[in1] = 0;
		if (registers.find(in2) == registers.end())
			registers[in2] = 0;

		bool doOperation = false;
		if (operation == "==" && registers[in2] == operationValue)
			doOperation = true;
		else if (operation == "!=" && registers[in2] != operationValue)
			doOperation = true;
		else if (operation == "<=" && registers[in2] <= operationValue)
			doOperation = true;
		else if (operation == ">=" && registers[in2] >= operationValue)
			doOperation = true;
		else if (operation == "> " && registers[in2] > operationValue)
			doOperation = true;
		else if (operation == "< " && registers[in2] < operationValue)
			doOperation = true;

		if (doOperation)
			if (instruction == "dec")
				registers[in1] -= increaseValue;
			else if (instruction == "inc")
				registers[in1] += increaseValue;

		if (registers[in1] > max2)
			max2 = registers[in1];
	}

	auto it = registers.begin();
	int max = it->second;
	it++;
	for (; it != registers.end(); ++it)
		if (it->second > max)
			max = it->second;

	cout << "Part I: " << max << endl << "Part II: " << max2 << endl;
	getchar();
	return 0;
}