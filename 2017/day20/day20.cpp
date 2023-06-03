#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct particle {
	int pos[3];
	int vel[3];
	int acc[3];
};

int main()
{
	ifstream input("input.txt");
	vector<particle> particles;
	string tmp;
	int po;
	while (getline(input, tmp))
	{
		particle p;
		po = tmp.find('p');
		p.pos[0] = stoi(tmp.substr(po + 3));
		po = tmp.find(',', po + 1);
		p.pos[1] = stoi(tmp.substr(po + 1));
		po = tmp.find(',', po + 1);
		p.pos[2] = stoi(tmp.substr(po + 1));
		po = tmp.find('v');
		p.vel[0] = stoi(tmp.substr(po + 3));
		po = tmp.find(',', po + 1);
		p.vel[1] = stoi(tmp.substr(po + 1));
		po = tmp.find(',', po + 1);
		p.vel[2] = stoi(tmp.substr(po + 1));
		po = tmp.find('a');
		p.acc[0] = stoi(tmp.substr(po + 3));
		po = tmp.find(',', po + 1);
		p.acc[1] = stoi(tmp.substr(po + 1));
		po = tmp.find(',', po + 1);
		p.acc[2] = stoi(tmp.substr(po + 1));
		particles.push_back(p);
	}
	int minacc = abs(particles[0].acc[0]) + abs(particles[0].acc[1]) + abs(particles[0].acc[2]);
	int minind = 0;
	for (int i = 0; i < particles.size(); i++)
	{
		if (abs(particles[i].acc[0]) + abs(particles[i].acc[1]) + abs(particles[i].acc[2]) < minacc)
		{
			minacc = abs(particles[i].acc[0]) + abs(particles[i].acc[1]) + abs(particles[i].acc[2]);
			minind = i;
		}
	}

	cout << "Part I: " << minind << endl;
	return 0;
}