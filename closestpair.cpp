/* CS331 Closest Pair Divide and Conquer Algorithm
 * From 10/10/2014 Class Discussion
 * 
 * Author: Bryan Thornbury
*/

#include <vector>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <stdio.h>
#include <cmath>

using namespace std;

typedef pair<float, float> ff;
typedef pair<int, ff > iff;
typedef vector<ff > vff;
typedef vector<iff > viff;

#define TRvff(it, v) \
	for(vff::iterator it = v.begin(); it != v.end(); ++it)

#define TRviff(it, v) \
	for(viff::iterator it = v.begin(); it != v.end(); ++it)

#define INF 2000000000;

class sortX {
public:
	bool operator() (ff &a, ff &b){
		return a.first < b.first;
	}
};

class sortY {
public:
	bool operator() (ff &a, ff &b){
		return a.second < b.second;
	}
};

float dist(ff a, ff b){
	return ((a.first - b.first) * (a.first - b.first)) + ((a.second - b.second) * (a.second - b.second));
}

//Change MidXValue when converting to float
float elevate(vff &sortedY, float d){
	float maxY = 0;
	int index = 0;
	TRvff(it, sortedY){
		maxY = it->second + d;
		for(vff::iterator it2 = (it+1); it2 != sortedY.end(); ++it2){
			if(it2->second > maxY) break;

			d = min(d,dist(*it, *it2));
			maxY = it->second + d;
		}
		index++;
	}

	return d;
}

float cRecurse(vff &sortedX, int start, int end){
	//printf("(%d, %d)\n", start, end);
	if(start == end) return INF;
	if(end-start == 1) return dist(sortedX[end], sortedX[start]);


	int mid = (start + end) / 2;

	vff sortedY(sortedX.begin() + start, sortedX.end() - (sortedX.size() - 1 - end));
	sort(sortedY.begin(), sortedY.end(), sortY());

	float d = min(cRecurse(sortedX, start, mid-1), cRecurse(sortedX, mid+1, end));
	d = min(d, elevate(sortedY, d));

	return d;
}


float closestPair(vff &points){
	vff sortedX(points);
	vff sortedY(points);

	sort(sortedX.begin(), sortedX.end(), sortX());
	//sort(sortedY.begin(), sortedY.end(), sortY());

	return sqrt(cRecurse(sortedX, 0, points.size() - 1));
}

float brute(vff &points){
	float d = INF;

	TRvff(it, points){
		for(vff::iterator it2 = (it+1); it2 != points.end(); ++it2){
			d = min(d, dist(*it, *it2));
		}
	}

	return sqrt(d);
}


int main(){
	srand(time(0));
	vff points;

	for(int i = 0; i < 100000; ++i){
		points.push_back(ff( (rand() % 400000 - 200000)/10.0, (rand() % 400000 - 200000)/10.0));
	}
	clock_t start = clock();
	float good = closestPair(points);
	start = clock() - start;
	printf("D&C - Value: %f, Time:%llu\n", good, (unsigned long long) start);

	start = clock();
	float bad = brute(points);
	start = clock() - start;
	printf("Brute - Value: %f, Time:%llu\n", bad,  (unsigned long long) start);

	return 0;
}
