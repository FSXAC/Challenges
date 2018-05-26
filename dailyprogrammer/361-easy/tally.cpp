#include <iostream>
#include <map>
#include <string>
#include <ctype.h>

using namespace std;

int main(void)
{
	map<char, int> tally;
	string scores;
	cin >> scores;

	for (char &c : scores)
	{
		char player = tolower(c);
		int addScore = player == c ? 1 : -1;
		if (tally.find(player) == tally.end())
		{
			tally.insert(pair<char, int>(player, addScore));
		}
		else
		{
			tally[player] += addScore;
		}
	}

	// output the result
	while (!tally.empty())
	{
		char maxPlayer;
		int maxScore;
		bool firstFlag = true;
		for (auto it = tally.begin(); it != tally.end(); it++)
		{
			if (firstFlag)
			{
				maxPlayer = it->first;
				maxScore = it->second;
				firstFlag = false;
			}
			else
			{
				if (it->second > maxScore)
				{
					maxPlayer = it->first;
					maxScore = it->second;
				}
			}
		}

		tally.erase(maxPlayer);
		cout << maxPlayer << ": " << maxScore << '\n';
	}

	return 0;
}