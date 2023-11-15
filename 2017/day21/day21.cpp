#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;

using Square = vector<string>;

string square_to_string(const Square &square)
{
	string s;
	for (const auto &row : square)
	{
		s += row;
	}
	return s;
}

void print_square(const Square &square)
{
	for (const auto &row : square)
	{
		cout << row << endl;
	}
}

map<string, Square> parse_rule(string line)
{
	map<string, Square> rules;

	auto pos = line.find(" => ");
	Square input_square, output_square;

	auto leftSide = stringstream(line.substr(0, pos));
	auto rightSide = stringstream(line.substr(pos + 4));
	string segment;

	while (getline(leftSide, segment, '/'))
	{
		input_square.push_back(segment);
	}
	while (getline(rightSide, segment, '/'))
	{
		output_square.push_back(segment);
	}

	// Generate all possible rotations and flips of the input square.
	for (int i = 0; i < 3; i++)
	{
		Square rotated_square;
		for (int j = 0; j < input_square.size(); j++)
		{
			string row;
			for (int k = input_square.size() - 1; k >= 0; k--)
			{
				row += input_square[k][j];
			}
			rotated_square.push_back(row);
		}
		input_square = rotated_square;
		rules.insert({square_to_string(input_square), output_square});

		reverse(input_square.begin(), input_square.end());
		rules.insert({square_to_string(input_square), output_square});
	}

	return rules;
}

vector<Square> split_image(const Square &image, int square_size)
{
	vector<Square> squares;
	for (int i = 0; i < image.size(); i += square_size)
	{
		for (int j = 0; j < image.size(); j += square_size)
		{
			Square square;
			for (int k = 0; k < square_size; k++)
			{
				square.push_back(image[i + k].substr(j, square_size));
			}
			squares.push_back(square);
		}
	}
	return squares;
}

Square enhance_square(Square &square, const map<string, Square> &rules)
{
	auto it = rules.find(square_to_string(square));
	if (it != rules.end())
	{
		return it->second;
	}
	// Flip and rotate the square until a matching rule is found.
	Square flipped_square = square;
	reverse(flipped_square.begin(), flipped_square.end());
	it = rules.find(square_to_string(flipped_square));
	if (it != rules.end())
	{
		return it->second;
	}
	for (int i = 0; i < 4; i++)
	{
		Square rotated_square;
		for (int j = 0; j < square.size(); j++)
		{
			string row;
			for (int k = square.size() - 1; k >= 0; k--)
			{
				row += square[k][j];
			}
			rotated_square.push_back(row);
		}
		square = rotated_square;
		it = rules.find(square_to_string(square));
		if (it != rules.end())
		{
			return it->second;
		}
		flipped_square = square;
		reverse(flipped_square.begin(), flipped_square.end());
		it = rules.find(square_to_string(flipped_square));
		if (it != rules.end())
		{
			return it->second;
		}
	}
	// If no matching rule is found, return the original square.
	return square;
}

Square join_squares(const vector<Square> &squares, int square_size)
{
	Square image;
	int num_squares_per_row = sqrt(squares.size());
	for (int i = 0; i < num_squares_per_row; i++)
	{
		for (int j = 0; j < square_size; j++)
		{
			string row;
			for (int k = 0; k < num_squares_per_row; k++)
			{
				row += squares[i * num_squares_per_row + k][j];
			}
			image.push_back(row);
		}
	}
	return image;
}

Square enhance_image(const Square &image, const map<string, Square> &rules, int num_iterations)
{
	Square current_image = image;

	for (int i = 0; i < num_iterations; i++)
	{
		int square_size = current_image.size() % 2 == 0 ? 2 : 3;
		vector<Square> squares = split_image(current_image, square_size);
		for (auto &square : squares)
		{
			square = enhance_square(square, rules);
		}
		current_image = join_squares(squares, square_size + 1);
	}
	return current_image;
}

int count_pixels_on(const Square &image)
{
	int c = 0;
	for (const auto &row : image)
	{
		c += count(row.begin(), row.end(), '#');
	}
	return c;
}

int main()
{
	ifstream input("input.txt");

	map<string, Square> rules;
	string tmp;
	while (getline(input, tmp))
	{
		for (auto rule : parse_rule(tmp))
		{
			rules.insert(rule);
		}
	}

	Square image = {".#.", "..#", "###"};

	cout << "Part I: " << count_pixels_on(enhance_image(image, rules, 5)) << endl;
	cout << "Part II: " << count_pixels_on(enhance_image(image, rules, 18)) << endl;
}
