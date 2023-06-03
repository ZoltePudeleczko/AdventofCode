#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
#include <iomanip>
#include <sstream>

using namespace std;

int main()
{
	ifstream input("input.txt");
	vector<int> lengths;
	vector<int> lengths2;
	string tmp;
	getline(input, tmp);
	int pos = -1;
	while (tmp.size() > 0)
	{
		lengths.push_back(stoi(tmp.substr(pos + 1)));
		if ((pos = tmp.find(',', pos + 1)) == string::npos)
			break;
	}
	for (int i = 0; i < tmp.size(); i++)
		lengths2.push_back((int)tmp[i]);
	vector<int> add = { 17, 31, 73, 47, 23 };
	lengths2.insert(lengths2.end(), add.begin(), add.end());

	/* Part One */
	vector<int> numbers;
	for (int i = 0; i < 256; i++)
		numbers.push_back(i);
	int half, skipsize = 0;
	pos = 0;
	for (int i = 0; i < lengths.size(); i++)
	{
		if (lengths[i] % 2 == 0)
			half = lengths[i] / 2;
		else
			half = (lengths[i] - 1) / 2;
		int pos2 = pos + lengths[i];
		for (int j = pos; j < pos + half; j++)
		{
			pos2--;
			swap(numbers[j % numbers.size()], numbers[pos2 % numbers.size()]);
		}
		pos += lengths[i];
		pos += skipsize;
		skipsize++;
	}
	cout << "Part I: " << numbers[0] * numbers[1] << endl;

	/* Part Two */
	vector<int> sparseHash;
	for (int i = 0; i < 256; i++)
		sparseHash.push_back(i);
	skipsize = 0;
	pos = 0;
	for (int k = 0; k < 64; k++)
	{
		for (int i = 0; i < lengths2.size(); i++)
		{
			if (lengths2[i] % 2 == 0)
				half = lengths2[i] / 2;
			else
				half = (lengths2[i] - 1) / 2;
			int pos2 = pos + lengths2[i];
			for (int j = pos; j < pos + half; j++)
			{
				pos2--;
				swap(sparseHash[j % sparseHash.size()], sparseHash[pos2 % sparseHash.size()]);
			}
			pos += lengths2[i];
			pos += skipsize;
			skipsize++;
		}
	}
	vector<int> denseHash;
	for (int i = 0; i < 16; i++)
	{
		denseHash.push_back(sparseHash[i * 16]);
		for (int j = 1; j < 16; j++)
			denseHash[i] = denseHash[i] ^ sparseHash[(i * 16) + j];
	}

	stringstream knotHashStream;
	for (int i = 0; i < denseHash.size(); i++)
		knotHashStream << std::setfill('0') << std::hex << denseHash[i];
	string knotHash = knotHashStream.str();

	cout << "Part II: " << knotHash << endl;
	return 0;
}