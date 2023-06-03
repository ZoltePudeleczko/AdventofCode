#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream input("input.txt");
	int step;
	input >> step;

	vector<int> buffer(1,0);
	auto it = buffer.begin();
	int pos = 0;
	for (int i = 1; i <= 2017; i++)
	{
		pos = (pos + step) % i;
		it = buffer.begin() + pos + 1;
		buffer.insert(it, i);
		pos++;
	}
	cout << "Part I: " << buffer[(pos + 1) % buffer.size()] << endl;

	buffer = vector<int>{ 0, 1 };
	pos = 1;
	for (int i = 2; i <= 50000000; i++)
	{
		pos = (pos + step) % i;
		if (pos == 0)
			buffer[1] = i;
		pos++;
	}
	cout << "Part II: " << buffer[1] << endl;
	return 0;
}