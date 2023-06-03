#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
#include <iomanip>
#include <sstream>
#include <bitset>


using namespace std;

string ToKnotHash(vector<int> in);
void CleanIt(int i, int j, bool grid[128][128]);

int main()
{
	ifstream input("input.txt");
	string key, t, bt;
	vector<int> keyv;
	vector<int> add = { 17, 31, 73, 47, 23 };
	getline(input, key);
	bitset<4> b;
	bool grid[128][128];
	int used = 0;
	for (int i = 0; i < 128; i++)
	{
		t = key + '-' + to_string(i);
		keyv.resize(0);
		for (int j = 0; j < t.size(); j++)
			keyv.push_back((int)t[j]);
		keyv.insert(keyv.end(), add.begin(), add.end());
		t = ToKnotHash(keyv);
		bt = "";
		for (int j = 0; j < t.size(); j++)
		{
			if ((int)t[j] > 96)
				b = bitset<4>((int)t[j] - 87);
			else
				b = bitset<4>((int)t[j] - 48);
			bt += b.to_string();
		}
		for (int j = 0; j < bt.size(); j++)
		{
			if (bt[j] == '1')
			{
				used++;
				grid[i][j] = true;
			}
			else
				grid[i][j] = false;
		}
	}
	int regions = 0;
	for (int i = 0; i < 128; i++)
		for (int j = 0; j < 128; j++)
			if (grid[i][j])
			{
				regions++;
				CleanIt(i, j, grid);
			}
	cout << "Part I: " << used << endl << "Part II: " << regions << endl;
	return 0;
}

void CleanIt(int i, int j, bool grid[128][128])
{
	grid[i][j] = false;
	if (i > 0 && grid[i - 1][j])
		CleanIt(i - 1, j, grid);
	if (j > 0 && grid[i][j-1])
		CleanIt(i, j - 1, grid);
	if (i < 127 && grid[i + 1][j])
		CleanIt(i + 1, j, grid);
	if (j < 127 && grid[i][j + 1])
		CleanIt(i, j + 1, grid);
}

string ToKnotHash(vector<int> in)
{
	vector<int> sparseHash;
	for (int i = 0; i < 256; i++)
		sparseHash.push_back(i);
	int skipsize = 0;
	int pos = 0;
	int half;
	for (int k = 0; k < 64; k++)
	{
		for (int i = 0; i < in.size(); i++)
		{
			if (in[i] % 2 == 0)
				half = in[i] / 2;
			else
				half = (in[i] - 1) / 2;
			int pos2 = pos + in[i];
			for (int j = pos; j < pos + half; j++)
			{
				pos2--;
				swap(sparseHash[j % sparseHash.size()], sparseHash[pos2 % sparseHash.size()]);
			}
			pos += in[i];
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
		knotHashStream << setw(2) << setfill('0') << hex << denseHash[i];
	return knotHashStream.str();
}