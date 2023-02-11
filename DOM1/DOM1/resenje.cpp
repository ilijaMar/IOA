#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


long long brojac1 = 0;
long long brojac2 = 0;

void A() {
	double suma = 7.77;


	double i, j, p, q;

	for (i = 1; i < 774; i += 1)
	{

		for (j = i; j < 774; j += 1)
		{

			for (p =j; p < 774; p += 1)
			{

				for (q = p; q < 774; q += 1)
				{
					brojac1 += 1;
					if (i + j + p + q == 777) {
						if (i * j * p * q == 777000000) {
							
							cout << "X1:" << i/100 << endl;
							cout << "X2:" << j/100 << endl;
							cout << "X3:" << p/100 << endl;
							cout << "X4:" << q/100 << endl;
							
						}
					}
				}

			}

		}

	}
	cout << "Brojac1:" << brojac1 << endl;

}
void B() {
	double suma = 7.77;


	double i, j, p, q;

	
	for (i = 0.01; i < 7.74; i += 0.01)
	{

		for (j = 0.01; j < 7.74-i; j += 0.01)
		{

			for (p = 0.01; p < 7.74-i-j; p += 0.01)
			{

				q = 7.77 - i - j - p;


				brojac2 += 1;
				
				if (i * j * p * q == 7.77) {

					
					cout << "X1:" << i << endl;
					cout << "X2:" << j << endl;
					cout << "X3:" << p << endl;
					cout << "X4:" << q << endl;
					
				}


			}

		}

	}
	cout << "Brojac2:" << brojac2 << endl;
}

int permutacije_bez_ponavljanja(int N, int* P) {
	int s;
	int* first = &P[0];
	int* last = &P[N - 1];
	int* k = last - 1;
	int* l = last;

	while (k > first) {
		if (*k < *(k + 1)) break;
		k--;
	}

	if (*k > * (k + 1)) return 0;

	while (l > k) {
		if (*l > * k)break;
		l--;
	}

	s = *k;
	*k = *l;
	*l = s;

	first = k + 1;

	while (first < last) {
		s = *first;
		*first = *last;
		*last = s;

		first++;
		last--;
	}
	return 1;
}
/*
int TSP(int grph[][vr], int p){ 
	vector<int> ver;
	for (int i = 0; i < vr; i++)
		if (i != p)
			ver.push_back(i);
	int m_p = INT_MAX; 
	do {
		int cur_pth = 0;
		int k = p;
		for (int i = 0; i < ver.size(); i++) {
			cur_pth += grph[k][ver[i]];
			k = ver[i];
		}
		cur_pth += grph[k][p];
		m_p = min(m_p, cur_pth);
	} while (permutacije_bez_ponavljanja(ver.begin(), ver.end()));
	return m_p;
}


*/







int main() {
	//A();
	//B();
	//if (brojac1 < brojac2) {
		//cout << "Algoritam A je brzi," << brojac2 / brojac1 << " puta" << endl;
	//}else cout << "Algoritam B je brzi," << brojac1 / brojac2 << " puta" << endl;
	int N = 5;
	int* P = new int[N];


	double tacke[8][2] = { { 62.0, 58.4}, //values of a graph in a form of matrix
	  { 57.5, 56.0 },
	  { 51.7, 56.0},
	  { 67.9, 19.6},
	  { 57.7, 42.1},
	  { 54.2, 29.1},
	  { 46.0, 45.1},
	  { 34.7, 45.1},
	};
	double rasojanja[8][8];
	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			rasojanja[i][j] = sqrt(pow((tacke[i][0] - tacke[j][0]),2)+pow((tacke[i][1] - tacke[j][1]),2));
		}
	}

	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			cout << rasojanja[i][j] << " ";
		}

		cout << endl;
	}
	for (int i = 0; i < N; i++)
	{
		P[i] = i + 1;
	}

	do {
		//for (int i = 0; i < N; i++)
			//printf("%2d ", P[i]);
		//printf("\n");
	} while (next_permutation(N, P));

	delete[]P;


	

}