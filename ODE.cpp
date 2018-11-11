#include<iostream>
#include<cmath>
#include <stdio.h>
using namespace std;
#define pi 3.1416925
#define h 0.1
#define iter 53 //53


int i,j =0;
double g = 10.0;
double c = 0.2;
double m = 0.2;
double cm = -1.0;

double x [iter], y [iter], v [iter], vx [iter], vy [iter];
void rungekuta(double angulo, double *x, double *y, double *v, double *vx , double *vy);

int main(){
	 /*FILE *MagnitudVelocidad;   
	MagnitudVelocidad = fopen("MagnitudVelocidad.dat","w");
	FILE *velocidadXY;     
	velocidadXY = fopen("velocidadXY.dat","w");
	FILE *posicion;     
	posicion = fopen("posicion.dat","w");

	double x[iter], y[iter], v[iter], vx[iter], vy[iter];
	// x, y, magnitud de velocidad , velocidad en x, velocidad en y
	
	x[0]=0;
	y[0]=0;
	//x[1]=3;
	//y[1]=4;
	v[0]=300;
	vx[0]=v[0]*cos(pi/4); 
	//vy[0]=v[0]*cos(pi/4); //la proyeccion de v sobre x,y es igual
	vy[0]=vx[0];
	
	
	//for (i; i<iteraciones; i++){
	//	v[i]=pow(((x[i]*x[i]) + (y[i]*y[i])) , 0.5);
	//	//v[i]=(x[i]*x[i]) + (y[i]*y[i]) ;
	//} 
	//cout << x[0] << " "<< y[0]<< endl;

	for (i=1; i< iter+1; i++){
		vx[i] = vx[i-1] + h*cm*vx[i-1]/v[i-1];
		vy[i] = vy[i-1] + h*(-g + cm*vy[i-1]/v[i-1]);
		v[i]=pow(((vx[i]*vx[i]) + (vy[i]*vy[i])) , 0.5);

		x[i] = x[i-1] + vx[i-1]*h + h*cm*x[i-1]/v[i-1];
		y[i] = y[i-1] + vy[i-1]*h + h*(-g*pow(h*i,2)*2 + cm*y[i-1]/v[i-1]);
	}
	//cout << v[iter-1] << "  VELOCID EN 0 "  << endl;
	//cout << v[iter] << "  VELOCID EN 1 "  << endl;
	//cout << iter-1 << ": " << x[iter-1] << " " << y[iter-1] << endl;
	//cout << iter << ": " << x[iter] << " " << y[iter] << endl;
	x[0]=0;
	y[0]=0;
	v[0]=300;
	vx[0]=v[0]*cos(pi/4);
	vy[0]=vx[0];

	for (i=0; i<iter; i++){
		//cout << i << " " <<vx[i] << " " << vy[i] << endl;
		
		fprintf(posicion,"%f %f",x[i] ,y[i]);
		fprintf(posicion,"\n");

		fprintf(velocidadXY,"%f %f",vx[i] ,vy[i]);
		fprintf(velocidadXY,"\n");

		fprintf(MagnitudVelocidad,"%f %f", h*i ,v[i]);
		fprintf(MagnitudVelocidad,"\n");
		//fprintf(velocidad, "%f\n" ,vy[i] );
	}
	fclose(velocidadXY);
	fclose(MagnitudVelocidad);
	fclose(posicion); **/
	rungekuta(pi/4, x, y, v, vx ,vy);
	/*rungekuta(10.0*180.0/pi, x, y, v, vx ,vy);
	rungekuta(20.0*180.0/pi, x, y, v, vx ,vy);
	rungekuta(30.0*180.0/pi, x, y, v, vx ,vy);
	rungekuta(30.0*180.0/pi, x, y, v, vx ,vy);
	rungekuta(30.0*180.0/pi, x, y, v, vx ,vy);*//
	return 0;
}
void rungekuta(double angulo, double *x, double *y, double *v, double *vx , double *vy){
	
	FILE *MagnitudVelocidad;   
	MagnitudVelocidad = fopen("MagnitudVelocidad.dat","w");
	FILE *velocidadXY;     
	velocidadXY = fopen("velocidadXY.dat","w");
	FILE *posicion;     
	posicion = fopen("posicion.dat","w");
	
	x[0]=0;
	y[0]=0;
	v[0]=300;
	vx[0]=v[0]*cos(angulo); 
	vy[0]=v[0]*sin(angulo); //la proyeccion de v sobre x,y es igual
	
	
	//for (i=0; i<iter; i++){
	//	x[i]=i;
	//	y[i]=i;
	///	vx[i] = i;
	//	vy[i] = i;
	//	v[i]=pow(((vx[i]*vx[i]) + (vy[i]*vy[i])) , 0.5);
		//cout << i << " " <<vx[i] << " " << vy[i] << endl;
	//}


	for (i=1; i< iter+1; i++){
		vx[i] = vx[i-1] + h*cm*vx[i-1]/v[i-1];
		vy[i] = vy[i-1] + h*(-g + cm*vy[i-1]/v[i-1]);
		v[i]=pow(((vx[i]*vx[i]) + (vy[i]*vy[i])) , 0.5);

		x[i] = x[i-1] + vx[i-1]*h + h*cm*x[i-1]/v[i-1];
		y[i] = y[i-1] + vy[i-1]*h + h*(-g*pow(h*i,2)*2 + cm*y[i-1]/v[i-1]);
	}
	
	x[0]=0;
	y[0]=0;
	v[0]=300;
	vx[0]=v[0]*cos(angulo); 
	vy[0]=v[0]*sin(angulo);

	for (i=0; i<iter; i++){
		//cout << i << " " <<vx[i] << " " << vy[i] << endl;
		
		fprintf(posicion,"%f %f",x[i] ,y[i]);
		fprintf(posicion,"\n");

		fprintf(velocidadXY,"%f %f",vx[i] ,vy[i]);
		fprintf(velocidadXY,"\n");

		fprintf(MagnitudVelocidad,"%f %f", h*i ,v[i]);
		fprintf(MagnitudVelocidad,"\n");
		//fprintf(velocidad, "%f\n" ,vy[i] );
	}
	fclose(velocidadXY);
	fclose(MagnitudVelocidad);
	fclose(posicion);
		
}
