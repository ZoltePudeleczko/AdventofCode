#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

struct state
{
	int if0Write;
	int if1Write;
	bool if0MoveRight;
	bool if1MoveRight;
	int if0NextState;
	int if1NextState;
};

int count_values(const map<int, bool> tape, bool value)
{
	int c = 0;
	for (auto kv : tape)
	{
		if (kv.second == value)
		{
			c += 1;
		}
	}
	return c;
}

int simulate(const vector<state> states, int steps)
{
	int currentState = 0;
	int cursor = 0;
	map<int, bool> tape;

	for (int i = 0; i < steps; i++)
	{
		bool containsValue = tape[cursor];

		if (containsValue)
		{
			if (states[currentState].if1Write == 0)
			{
				tape[cursor] = 0;
			}

			if (states[currentState].if1MoveRight)
			{
				cursor += 1;
			}
			else
			{
				cursor -= 1;
			}

			currentState = states[currentState].if1NextState;
		}
		else
		{
			if (states[currentState].if0Write == 1)
			{
				tape[cursor] = 1;
			}

			if (states[currentState].if0MoveRight)
			{
				cursor += 1;
			}
			else
			{
				cursor -= 1;
			}

			currentState = states[currentState].if0NextState;
		}
	}

	return count_values(tape, true);
}

int main()
{
	ifstream input("input.txt");
	string tmp;

	vector<state> states;
	int steps;

	while (getline(input, tmp))
	{
		int stepsPlace = tmp.find("Perform a diagnostic checksum after");
		if (stepsPlace != -1)
		{
			steps = stoi(tmp.substr(stepsPlace + 36));
			break;
		}
	}

	while (getline(input, tmp))
	{
		int find = tmp.find("In state");

		if (tmp.find("In state") != -1)
		{
			state newState = state();
			getline(input, tmp);
			getline(input, tmp);
			newState.if0Write = stoi(tmp.substr(tmp.find("Write the value") + 15));

			getline(input, tmp);
			newState.if0MoveRight = tmp.find("Move one slot to the right") != -1;

			getline(input, tmp);
			newState.if0NextState = tmp[tmp.find("Continue with state") + 20] - 'A';

			getline(input, tmp);
			getline(input, tmp);
			newState.if1Write = stoi(tmp.substr(tmp.find("Write the value") + 15));

			getline(input, tmp);
			newState.if1MoveRight = tmp.find("Move one slot to the right") != -1;

			getline(input, tmp);
			newState.if1NextState = tmp[tmp.find("Continue with state") + 20] - 'A';

			states.push_back(newState);
		}
	}

	cout << "Part I: " << simulate(states, steps) << endl;
}