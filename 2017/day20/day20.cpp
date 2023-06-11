#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct particle
{
	int pos[3];
	int vel[3];
	int acc[3];
	bool removed;
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

	// Part I
	int minacc = INT_MAX;
	int minind = -1;
	for (int i = 0; i < particles.size(); i++)
	{
		if (abs(particles[i].acc[0]) + abs(particles[i].acc[1]) + abs(particles[i].acc[2]) < minacc)
		{
			minacc = abs(particles[i].acc[0]) + abs(particles[i].acc[1]) + abs(particles[i].acc[2]);
			minind = i;
		}
	}

	cout << "Part I: " << minind << endl;

	// Part II
	int lastCollision = 0;
	while (lastCollision < 100)
	{
		for (int i = 0; i < particles.size(); i++)
		{
			if (particles[i].removed)
				continue;

			particles[i].vel[0] += particles[i].acc[0];
			particles[i].vel[1] += particles[i].acc[1];
			particles[i].vel[2] += particles[i].acc[2];
			particles[i].pos[0] += particles[i].vel[0];
			particles[i].pos[1] += particles[i].vel[1];
			particles[i].pos[2] += particles[i].vel[2];
		}

		bool collision = false;
		for (int i = 0; i < particles.size(); i++)
		{
			if (particles[i].removed)
				continue;

			for (int j = i + 1; j < particles.size(); j++)
			{
				if (particles[j].removed)
					continue;

				if (particles[i].pos[0] == particles[j].pos[0] && particles[i].pos[1] == particles[j].pos[1] && particles[i].pos[2] == particles[j].pos[2])
				{
					particles[i].removed = true;
					particles[j].removed = true;
					collision = true;
				}
			}
		}

		if (!collision)
			lastCollision++;
		else
			lastCollision = 0;
	}

	int count = 0;
	for (auto particle : particles)
	{
		if (!particle.removed)
			count++;
	}

	cout << "Part II: " << count << endl;
}