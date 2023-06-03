#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct node {
	string name;
	int weight;
	int combinedWeight = 0;
	vector<string> childs;
	vector<node*> childsPointers;
	bool hasParent = false;
};

int combineWeights(node* p);
int findProblem(node* p, int wantedWeight = 0);

int main()
{
	vector<node> tower;
	string tmp;
	ifstream input("input.txt");
	int pos, pos2;
	while (getline(input, tmp))
	{
		node t;
		pos = tmp.find('(');
		t.name = tmp.substr(0, pos - 1);
		t.weight = stoi(tmp.substr(pos + 1));

		if ((pos = tmp.find("->")) != string::npos)
		{
			pos = tmp.find(' ', pos);
			while ((pos2 = tmp.find(',', pos)) != string::npos)
			{
				t.childs.push_back(tmp.substr(pos + 1, pos2 - pos - 1));
				pos = pos2 + 1;
			}
			t.childs.push_back(tmp.substr(pos + 1));
		}
		tower.push_back(t);
	}

	for (int i = 0; i < tower.size(); i++)
	{
		for (int j = 0; j < tower[i].childs.size(); j++)
		{
			for (int k = 0; k < tower.size(); k++)
			{
				if (tower[k].hasParent)
					continue;
				if (tower[k].name == tower[i].childs[j])
				{
					tower[k].hasParent = true;
					tower[i].childsPointers.push_back(&tower[k]);
					break;
				}
			}
		}
	}

	node* root;
	for (int i = 0; i < tower.size(); i++)
	{
		if (!tower[i].hasParent)
		{
			root = &tower[i];
		}
	}
	combineWeights(root);
	int balance = findProblem(root);

	cout << "Part I: " << root->name << endl << "Part II: " << balance << endl;
	return 0;
}

int combineWeights(node* p)
{
	p->combinedWeight = p->weight;
	for (int i = 0; i < p->childsPointers.size(); i++)
	{
		p->combinedWeight += combineWeights(p->childsPointers[i]);
	}
	return p->combinedWeight;
}

int findProblem(node* p, int wantedWeight)
{
	if (p->childs.size() == 0)
		return wantedWeight;
	if (p->childs.size() == 1)
		return findProblem(p->childsPointers[0], wantedWeight - p->combinedWeight);
	if (p->childs.size() == 2)
		return findProblem(p->childsPointers[0], p->childsPointers[1]->combinedWeight);
	int ww = p->childsPointers[0]->combinedWeight;
	int k = 0;

	for (int i = 1; i < p->childs.size(); i++)
		if (p->childsPointers[i]->combinedWeight == ww)
			k++;
	if (k == 0)
		return findProblem(p->childsPointers[0], p->childsPointers[1]->combinedWeight);
	if (k == p->childs.size() - 1)
		return p->weight + (wantedWeight - p->combinedWeight);

	for (int i = 0; i < p->childs.size(); i++)
		if (p->childsPointers[i]->combinedWeight != ww)
			k = i;
	return findProblem(p->childsPointers[k], ww);
}