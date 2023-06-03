#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct component {
	int port1;
	int port2;
	bool used = false;
};

int BuildBridges(vector<component> &components, int ind, int myVal, int myLength, int &maxLength);
int BuildLongestBridges(vector<component> &components, int ind, int myVal, int myLength, int &maxLength);

int main()
{
	ifstream input("input.txt");
	vector<component> components;
	string tmp;
	while (getline(input, tmp))
	{
		component t;
		t.port1 = stoi(tmp.substr(0));
		t.port2 = stoi(tmp.substr(tmp.find('/') + 1));
		if (t.port1 != 0 && t.port2 == 0)
			swap(t.port1, t.port2);
		components.push_back(t);
	}
	int tVal, maxVal = 0;
	int maxLength = 0;
	for (int i = 0; i < components.size(); i++)
	{
		if (components[i].port1 != 0)
			continue;

		tVal = BuildBridges(components, i, components[i].port1 + components[i].port2, 1, maxLength);
		if (tVal > maxVal)
			maxVal = tVal;
	}
	int maxLongVal = 0;
	for (int i = 0; i < components.size(); i++)
	{
		if (components[i].port1 != 0)
			continue;

		tVal = BuildLongestBridges(components, i, components[i].port1 + components[i].port2, 1, maxLength);
		if (tVal > maxLongVal)
			maxLongVal = tVal;
	}
	cout << "Part I: " << maxVal << endl << "Part II: " << maxLongVal << endl;
	return 0;
}

int BuildBridges(vector<component> &components, int ind, int myVal, int myLength, int &maxLength)
{
	components[ind].used = true;
	if (myLength > maxLength)
		maxLength = myLength;
	int tVal, myMax = myVal;
	for (int i = 0; i < components.size(); i++)
	{
		if (components[i].used)
			continue;

		if (components[i].port1 == components[ind].port2)
		{
			tVal = BuildBridges(components, i, myVal + components[i].port1 + components[i].port2, myLength + 1, maxLength);
			if (tVal > myMax)
				myMax = tVal;
		}
		else if (components[i].port2 == components[ind].port2)
		{
			swap(components[i].port1, components[i].port2);
			tVal = BuildBridges(components, i, myVal + components[i].port1 + components[i].port2, myLength + 1, maxLength);
			if (tVal > myMax)
				myMax = tVal;
		}
	}
	components[ind].used = false;
	return myMax;
}

int BuildLongestBridges(vector<component> &components, int ind, int myVal, int myLength, int &maxLength)
{
	components[ind].used = true;
	int tVal, myMax = myVal;
	for (int i = 0; i < components.size(); i++)
	{
		if (components[i].used)
			continue;

		if (components[i].port1 == components[ind].port2)
		{
			tVal = BuildLongestBridges(components, i, myVal + components[i].port1 + components[i].port2, myLength + 1, maxLength);
			if (tVal > myMax)
				myMax = tVal;
		}
		else if (components[i].port2 == components[ind].port2)
		{
			swap(components[i].port1, components[i].port2);
			tVal = BuildLongestBridges(components, i, myVal + components[i].port1 + components[i].port2, myLength + 1, maxLength);
			if (tVal > myMax)
				myMax = tVal;
		}
	}
	components[ind].used = false;
	if (myMax == myVal && myLength < maxLength)
		return -1;
	return myMax;
}