#include <iostream>
#include <bitset>

using namespace std;

static int AFactor = 16807;
static int BFactor = 48271;
static int divideValue = 2147483647;
static int AStart = 591;
static int BStart = 393;
static int pairs = 40000000;
static int pairs2 = 5000000;

int main()
{
	long long aValue = AStart;
	long long bValue = BStart;

	bitset<16> a;
	bitset<16> b;
	int judge = 0;
	for (int i = 0; i < pairs; i++)
	{
		aValue = (aValue * AFactor) % divideValue;
		bValue = (bValue * BFactor) % divideValue;
		a = bitset<16>(aValue);
		b = bitset<16>(bValue);
		if (a == b)
			judge++;
	}

	aValue = AStart;
	bValue = BStart;
	int judge2 = 0;
	for (int i = 0; i < pairs2; i++)
	{
		do
		{
			aValue = (aValue * AFactor) % divideValue;
		} while (aValue % 4 != 0);
		do
		{
			bValue = (bValue * BFactor) % divideValue;
		} while (bValue % 8 != 0);
		a = bitset<16>(aValue);
		b = bitset<16>(bValue);
		if (a == b)
			judge2++;
	}

	cout << "Part I: " << judge << endl << "Part II: " << judge2 << endl;
	return 0;
}