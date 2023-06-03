#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream input("input.txt");
	string in;
	getline(input, in);
	int sum1 = 0;
	int sum2 = 0;
	int ind1, ind2;
	for (int i = 0; i < in.size(); i++)
	{
		ind1 = (i + 1) % in.size();
		ind2 = (i + (in.size() / 2)) % in.size();
		if (in[i] == in[ind1])
			sum1 += (int)in[i] - 48;
		if (in[i] == in[ind2])
			sum2 += (int)in[i] - 48;
	}
	cout << in << endl << "Part I: " << sum1 << endl << "Part II: " << sum2 << endl;
	return 0;
}
