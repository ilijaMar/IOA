#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;



const int N = 8;
const int M = 12;
double TSPA(double grph[][N], int p){
	vector<int> ver;
	
	vector<int> path;

	for (int i = 0; i < N; i++)
		ver.push_back(i);
			
	
	double m_p = INT_MAX;
	do {
		double cur_pth = 0;
		

		for (int i = 0; i < ver.size()-1; i++) {

			cur_pth += grph[ver[i]][ver[i+1]];
			
		}

		double mold = m_p;
		m_p = min(m_p, cur_pth);
		if(mold!=m_p)     
			path = ver;

	} while (next_permutation(ver.begin(), ver.end()));

	for (int i : path)
		cout << i+1 << ' ';

	return m_p;
}
double TSPB(double grph[][M], int p) {
	vector<int> ver;
	vector<int> path;

	for (int i = 0; i < M; i++)
		ver.push_back(i);
		

	double m_p = INT_MAX;
	do {
		double cur_pth = 0;
		

		for (int i = 0; i < ver.size() - 1; i++) {
			

			cur_pth += grph[ver[i]][ver[i + 1]];

		}

		double mold = m_p;
		m_p = min(m_p, cur_pth);
		if (mold != m_p)
			path = ver;

	} while (next_permutation(ver.begin(), ver.end()));

	for (int i : path)
		cout << i+1 << ' ';

	return m_p;
}









int main() {
	
	int* P = new int[8];


	double tackeA[N][2] = { { 62.0, 58.4}, 
	  { 57.5, 56.0 },
	  { 51.7, 56.0},
	  { 67.9, 19.6},
	  { 57.7, 42.1},
	  { 54.2, 29.1},
	  { 46.0, 45.1},
	  { 34.7, 45.1},
	};

	double tackeB[M][2] = { { 62.0, 58.4},
	  { 57.5, 56.0 },
	  { 51.7, 56.0},
	  { 67.9, 19.6},
	  { 57.7, 42.1},
	  { 54.2, 29.1},
	  { 46.0, 45.1},
	  { 34.7, 45.1},
	  { 45.7, 25.1},
	  { 34.7, 26.4},
	  { 28.4, 31.7},
	  { 33.4, 60.5}
	};
	double rasojanjaA[N][N];
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			rasojanjaA[i][j] = sqrt(pow((tackeA[i][0] - tackeA[j][0]), 2) + pow((tackeA[i][1] - tackeA[j][1]), 2));
		}
	}

	double rasojanjaB[M][M];
	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < M; j++)
		{
			rasojanjaB[i][j] = sqrt(pow((tackeB[i][0] - tackeB[j][0]), 2) + pow((tackeB[i][1] - tackeB[j][1]), 2));
		}
	}

	
	
	int p = 0;
	cout << "\nResenje pod A: " << TSPA(rasojanjaA, p) << endl;

	int q = 0;
	cout << "\nResenje pod B: " << TSPB(rasojanjaB, q) << endl;

	delete[]P;




}