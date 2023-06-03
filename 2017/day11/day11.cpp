#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
	ifstream input("input.txt");

	char a;
	int row, col;
	row = col = 0;
	int maxDistance = 0;
	while (!input.eof())
	{
		input.get(a);
		if (a == 'n')
		{
			input.get(a);
			if (a == ',') //north
			{
				row--;
			}
			else if (a == 'e') //north-east
			{
				input.get(a);
				row--;
				col++;
			}
			else if (a == 'w') //north-south
			{
				input.get(a);
				col--;
			}
		}
		else if (a == 's')
		{
			input.get(a);
			if (a == ',') //south
			{
				row++;
			}
			else if (a == 'e') //south-east
			{
				input.get(a);
				col++;
			}
			else if (a == 'w') //south-west
			{
				input.get(a);
				row++;
				col--;
			}
		}
		if (((abs(col) + abs(row) + abs(col + row)) / 2) > maxDistance)
			maxDistance = (abs(col) + abs(row) + abs(col + row)) / 2;
	}
	cout << "Part I: " << (abs(col) + abs(row) + abs(col + row)) / 2 << endl << "Part II: " << maxDistance << endl;

	return 0;
}