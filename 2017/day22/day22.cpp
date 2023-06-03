#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct Line {
	string data;
	Line* up = nullptr;
	Line* down = nullptr;
};

enum Turn {
	Up, Down, Left, Right
};

void PartOne(Line* head, Line* p, int posx);
void PartTwo(Line* head, Line* p, int posx);


int main()
{
	ifstream input("input.txt");
	string tmp;
	Line* head = nullptr;
	Line* p = nullptr;
	int n = 0;
	while (getline(input, tmp))
	{
		n++;
		Line* t = new Line;
		t->data = tmp;
		t->up = p;
		if (p)
		{
			p->down = t;
		}
		if (!head)
			head = t;
		p = t;
	}
	p = head;
	for (int i = 0; i < (n / 2); i++)
		p = p->down;
	int posx = p->data.size() / 2;
	cout << "Which part (1/2)?\n";
	int launchPart;
	cin >> launchPart;
	switch (launchPart)
	{
	case 1:
		PartOne(head, p, posx);
		break;
	case 2:
		PartTwo(head, p, posx);
		break;
	}
	return 0;
}

void PartOne(Line* head, Line* p, int posx)
{
	int infectionBursts = 0;
	Turn direction = Up;
	for (int i = 0; i < 10000; i++)
	{
		if (p->data[posx] == '#')
		{
			p->data[posx] = '.';
			switch (direction)
			{
			case Up:
				direction = Right;
				break;
			case Down:
				direction = Left;
				break;
			case Right:
				direction = Down;
				break;
			case Left:
				direction = Up;
				break;
			}
		}
		else
		{
			p->data[posx] = '#';
			infectionBursts++;
			switch (direction)
			{
			case Up:
				direction = Left;
				break;
			case Down:
				direction = Right;
				break;
			case Right:
				direction = Up;
				break;
			case Left:
				direction = Down;
				break;
			}
		}

		switch (direction)
		{
		case Up:
			if (!p->up)
			{
				Line* t = new Line;
				t->down = p;
				t->data = string(p->data.size(), '.');
				p->up = t;
				if (p == head)
					head = t;
			}
			p = p->up;
			break;
		case Down:
			if (!p->down)
			{
				Line* t = new Line;
				t->up = p;
				t->data = string(p->data.size(), '.');
				p->down = t;
			}
			p = p->down;
			break;
		case Right:
			posx++;
			if (posx > p->data.size() - 1)
			{
				Line* tp = head;
				while (tp)
				{
					tp->data += ".";
					tp = tp->down;
				}
			}
			break;
		case Left:
			posx--;
			if (posx < 0)
			{
				Line* tp = head;
				while (tp)
				{
					tp->data = "." + tp->data;
					tp = tp->down;
				}
				posx = 0;
			}
			break;
		}
	}
	cout << "Part I: " << infectionBursts << endl;
}

void PartTwo(Line* head, Line* p, int posx)
{
	int infectionBursts = 0;
	Turn direction = Up;
	for (int i = 0; i < 10000000; i++)
	{
		if (p->data[posx] == '.')
		{
			p->data[posx] = 'W';
			switch (direction)
			{
			case Up:
				direction = Left;
				break;
			case Down:
				direction = Right;
				break;
			case Right:
				direction = Up;
				break;
			case Left:
				direction = Down;
				break;
			}
		}
		else if (p->data[posx] == 'W')
		{
			infectionBursts++;
			p->data[posx] = '#';
		}
		else if (p->data[posx] == '#')
		{
			p->data[posx] = 'F';
			switch (direction)
			{
			case Up:
				direction = Right;
				break;
			case Down:
				direction = Left;
				break;
			case Right:
				direction = Down;
				break;
			case Left:
				direction = Up;
				break;
			}
		}
		else if (p->data[posx] == 'F')
		{
			p->data[posx] = '.';
			switch (direction)
			{
			case Up:
				direction = Down;
				break;
			case Down:
				direction = Up;
				break;
			case Right:
				direction = Left;
				break;
			case Left:
				direction = Right;
				break;
			}
		}

		switch (direction)
		{
		case Up:
			if (!p->up)
			{
				Line* t = new Line;
				t->down = p;
				t->data = string(p->data.size(), '.');
				p->up = t;
				if (p == head)
					head = t;
			}
			p = p->up;
			break;
		case Down:
			if (!p->down)
			{
				Line* t = new Line;
				t->up = p;
				t->data = string(p->data.size(), '.');
				p->down = t;
			}
			p = p->down;
			break;
		case Right:
			posx++;
			if (posx > p->data.size() - 1)
			{
				Line* tp = head;
				while (tp)
				{
					tp->data += ".";
					tp = tp->down;
				}
			}
			break;
		case Left:
			posx--;
			if (posx < 0)
			{
				Line* tp = head;
				while (tp)
				{
					tp->data = "." + tp->data;
					tp = tp->down;
				}
				posx = 0;
			}
			break;
		}
	}
	cout << "Part II: " << infectionBursts << endl;
}