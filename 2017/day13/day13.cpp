#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

struct Firewall {
	int depth;
	int range;

	int fullLoop()
	{
		return (range - 1) * 2;
	}
};

int main()
{
	ifstream input("input.txt");
	vector<Firewall> firewalls;
	string tmp;

	while (getline(input, tmp))
	{
		Firewall t;
		t.depth = stoi(tmp);
		t.range = stoi(tmp.substr(tmp.find(' ')));
		firewalls.push_back(t);
	}

	bool caught;
	int sum = 0;
	int delay = 0;
	do
	{
		caught = false;
		for (int i = 0; i < firewalls.size(); i++)
		{
			if ((delay + firewalls[i].depth) % firewalls[i].fullLoop() == 0)
			{
				caught = true;
				if (delay == 0)
					sum += firewalls[i].range * firewalls[i].depth;
				else
					break;
			}
		}
		delay++;
	} while (caught);
	cout << "Part I: " << sum << endl << "Part II: " << delay << endl;
	return 0;
}