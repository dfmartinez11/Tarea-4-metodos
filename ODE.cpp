#include<iostream>
#include<cmath>
using namespace std;
int i,j =0;
double g = 10.0;
double c = 0.2;
double m = 0.2;


int main(){
	
	double x [10];
	double y [10];
	double v [10];
	double vx [10];
	double vy [10];
	x[0]=0;
	y[0]=0;
	//x[1]=3;
	//y[1]=4;
	v[0]=300;
	vx[0]=v[0]*cos(3.141692/4);
	vy[0]=v[0]*sin(3.141692/4);
	for (i; i<10; i++){
		v[i]=pow(((x[i]*x[i]) + (y[i]*y[i])) , 0.5);
		//v[i]=(x[i]*x[i]) + (y[i]*y[i]) ;
	}
	
	
	cout << g << c << m<< endl;
	cout << vx[0] << endl;
	return 0;
}
