#include <iostream>
#include <math.h>
#include <vector>
#include <string>

using namespace std;

double tanh(double x) {
	return (((exp(x)) - (exp(-1 * x))) / ((exp(x)) + (exp(-1 * x))));
}

double sech(double x) {
	return (2 / ((exp(x)) + (exp(-1 * x))));
}

double tanh_deriv(double x) {
	return (sech(x)*sech(x));
}

vector<double> forward(vector<double> x, vector<vector<double>> w1, vector<vector<double>> w2, bool predict) {
	vector<double> a1;
	vector<double> z1;
	vector<double> a2;
	vector<double> z2;
	for (int i = 0; i < w1[0].size(); i++) {
		double sum = 0;
		for (int j = 0; j < x.size(); j++) {
			sum += x[j] * w1[j][i];
		}
		a1.push_back(sum);
		z1.push_back(tanh(sum));
	}
	z1.push_back(1);
	for (int i = 0; i < w2[0].size(); i++) {
		double sum = 0;
		for (int j = 0; j < z1.size(); j++) {
			sum += z1[j] * w2[j][i];
		}
		a2.push_back(sum);
		z2.push_back(tanh(sum));
	}
	if (predict) {
		return z2;
	}
	vector<double> result;
	result.push_back(a1);
	result.push_back(z1);
	result.push_back(a2);
	result.push_back(z2);
	return result;
