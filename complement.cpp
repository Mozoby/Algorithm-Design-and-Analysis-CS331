#include <stdio.h>
#include <vector>

using namespace std;

vector<int>  complementaryProducts(vector<int> a, int n){

	vector<int> b(n);
	vector<int>  p;
	(p).resize(n);

	//construct backwards multiplication array b[0] is empty
	b[n-1] = a[n-1];
	for(int i = n-2; i >= 1; i--)
		b[i] = b[i+1] * a[i];

	long long z = 1L;
	(p)[0] = b[1];

	for(int i = 1; i <= n-2; i++){
		z*=a[i-1];
		(p)[i] = z * b[i+1];
	}

	(p)[n-1] = z * a[n-2];

	return p;
}

int main(){
	vector<int> a(10);

	int totalProduct = 1;
	for(int i = 0; i < a.size(); i++){
		a[i] = i + 1;
		totalProduct *= a[i];
	}

	vector<int>  p = complementaryProducts(a, a.size());

	for(int i = 0; i < a.size(); i++){
		if((p)[i] == (totalProduct/a[i]))
			printf("%d\n", (p)[i]);
		else
			printf("no %d %d\n", (p)[i], totalProduct);
	}
}