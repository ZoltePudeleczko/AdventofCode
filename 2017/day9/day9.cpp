#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream input("input.txt");
	char a;

	bool inGarbage = false;
	int openGroups = 0;
	int score = 0;
	int garbageCount = 0;
	while (!input.eof())
	{
		input.get(a);
		
		if (a == '!')
		{
			input.get(a);
			continue;
		}

		if (inGarbage)
		{
			if (a == '>')
				inGarbage = false;
			else
				garbageCount++;
		}
		else
		{
			if (a == '{')
			{
				openGroups++;
				score += openGroups;
			}
			if (a == '}')
				openGroups--;
			if (a == '<')
				inGarbage = true;
		}
	}

	cout << "Part I: " << score << endl << "Part II: " << garbageCount << endl;
	return 0;
}