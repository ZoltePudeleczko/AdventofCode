#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ifstream input("input.txt");
	vector<string> diagram;
	string tmp;
	while (getline(input, tmp))
		diagram.push_back(tmp);

	string letters;
	int r = 0; //row
	int c = diagram[0].find('|'); //column
	bool up, right, left, down;
	up = right = left = false;
	down = true;
	int steps = 0;
	while (diagram[r][c] != ' ')
	{
		steps++;
		if (diagram[r][c] == '+')
		{
			if (up || down)
			{
				up = false;
				down = false;
				if (c > 0 && diagram[r][c - 1] != ' ')
					left = !left;
				if (c + 1 < diagram[r].size() && diagram[r][c + 1] != ' ')
					right = !right;
			}
			else if (left || right)
			{
				left = false;
				right = false;
				if (r > 0 && diagram[r - 1][c] != ' ')
					up = !up;
				if (r + 1 < diagram.size() && diagram[r + 1][c] != ' ')
					down = !down;
			}
		}
		else if (diagram[r][c] != '-' && diagram[r][c] != '|')
			letters.push_back(diagram[r][c]);

		if (up)
			r--;
		if (down)
			r++;
		if (left)
			c--;
		if (right)
			c++;
	}
	cout << "Part I: " << letters << endl << "Part II: " << steps << endl;
	return 0;
}