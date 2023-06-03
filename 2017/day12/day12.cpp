#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void checkConnection(vector<vector<int>>& p, vector<bool>& c, int i);

int main()
{
	ifstream input("input.txt");
	string tmp, a;

	vector<vector<int>> programs;
	int s, pos, i = 0;
	while (getline(input, tmp))
	{
		vector<int> t;
		pos = tmp.find('>') + 1;
		do 
		{
			s = stoi(tmp.substr(pos + 1));
			if (s != i)
				t.push_back(s);
			
		} while ((pos = tmp.find(',', pos + 1)) != string::npos);
		programs.push_back(t);
		i++;
	}
	
	vector<bool> connectedTo0;
	connectedTo0.push_back(true);
	for (int i = 1; i < programs.size(); i++)
		connectedTo0.push_back(false);
	checkConnection(programs, connectedTo0, 0);

	int groupSize = 0;
	for (int i = 0; i < connectedTo0.size(); i++)
		if (connectedTo0[i])
			groupSize++;

	int groupsNumber = 1;
	for (int i = 0; i < connectedTo0.size(); i++)
		if (!connectedTo0[i])
		{
			groupsNumber++;
			checkConnection(programs, connectedTo0, i);
		}


	cout << "Part I: " << groupSize << endl << "Part II: " << groupsNumber << endl;
	return 0;
}

void checkConnection(vector<vector<int>>& p, vector<bool>& c, int i)
{
	for (int j = 0; j < p[i].size(); j++)
	{
		if (c[p[i][j]] == false)
		{
			c[p[i][j]] = true;
			checkConnection(p, c, p[i][j]);
		}
	}
}
