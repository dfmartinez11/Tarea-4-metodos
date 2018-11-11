#include<iostream>
#include<cmath>
#include <stdio.h>
using namespace std;
#define pi 3.1416925
#define h 0.11
#define iter 60 //53


int i,j =0;
double g = 10.0;
double c = 0.2;
double m = 0.2;
double cm = -1.0;

double x[iter], y[iter], v[iter], vx[iter], vy[iter];

void rungekuta40(double *x, double *y, double *v, double *vx , double *vy);
void rungekuta(double angulo, double *x, double *y, double *v, double *vx , double *vy);
void anularVectores(double *x, double *y, double *v, double *vx , double *vy);

int main(){

	rungekuta40(x, y, v, vx ,vy);
	anularVectores(x, y, v, vx ,vy);
	//for (i=0; i<iter; i++){
	//cout << x[i] << " " << y[i] << endl;
	//}

	rungekuta(10.0*pi/180 , x, y, v, vx ,vy);
	FILE *posicion10;   
	posicion10 = fopen("10_posicion.dat","w");
	for (i=0; i<iter; i++){
				
		fprintf(posicion10,"%f %f",x[i] ,y[i]);
		fprintf(posicion10,"\n");
	}
	anularVectores(x, y, v, vx ,vy);
	

	rungekuta(20.0*pi/180 , x, y, v, vx ,vy);
	FILE *posicion20;   
	posicion20 = fopen("20_posicion.dat","w");
	for (i=0; i<iter; i++){
		for (j=1; j<iter ; j++){
			if (y[i])
		{		
		fprintf(posicion20,"%f %f",x[i] ,y[i]);
		fprintf(posicion20,"\n");
	}
	anularVectores(x, y, v, vx ,vy);


	rungekuta(30.0*pi/180 , x, y, v, vx ,vy);
	FILE *posicion30;   
	posicion30 = fopen("30_posicion.dat","w");
	for (i=0; i<iter; i++){
				
		fprintf(posicion30,"%f %f",x[i] ,y[i]);
		fprintf(posicion30,"\n");
	}
	anularVectores(x, y, v, vx ,vy);


	rungekuta(50.0*pi/180 , x, y, v, vx ,vy);
	FILE *posicion50;   
	posicion50 = fopen("50_posicion.dat","w");
	for (i=0; i<iter; i++){
				
		fprintf(posicion50,"%f %f",x[i] ,y[i]);
		fprintf(posicion50,"\n");
	}
	anularVectores(x, y, v, vx ,vy);


	rungekuta(60.0*pi/180 , x, y, v, vx ,vy);
	FILE *posicion60;   
	posicion60 = fopen("60_posicion.dat","w");
	for (i=0; i<iter; i++){
				
		fprintf(posicion60,"%f %f",x[i] ,y[i]);
		fprintf(posicion60,"\n");
	}
	anularVectores(x, y, v, vx ,vy);

	
	rungekuta(70.0*pi/180, x, y, v, vx ,vy);
	FILE *posicion70;   
	posicion70 = fopen("70_posicion.dat","w");
	for (i=0; i<iter; i++){
				
		fprintf(posicion70,"%f %f",x[i] ,y[i]);
		fprintf(posicion70,"\n");
	}
	anularVectores(x, y, v, vx ,vy);
		
	return 0;

}
void rungekuta40(double *x, double *y, double *v, double *vx , double *vy){
	
	FILE *MagnitudVelocidad;   
	MagnitudVelocidad = fopen("MagnitudVelocidad.dat","w");
	FILE *velocidadXY;     
	velocidadXY = fopen("velocidadXY.dat","w");
	FILE *posicion;     
	posicion = fopen("posicion.dat","w");
	
	x[0]=0.0;
	y[0]=0.0;
	v[0]=300;
	vx[0]=v[0]*cos(40*pi/180); 
	vy[0]=vx[0]; // las proyecciones de v sobre x,y son las mismas

	/*for (i=1; i< iter+1; i++){
		vx[i] = vx[i-1] + h*cm*vx[i-1]/v[i-1];
		vy[i] = vy[i-1] + h*(-g + cm*vy[i-1]/v[i-1]);
		v[i]=pow(((vx[i]*vx[i]) + (vy[i]*vy[i])) , 0.5);

		x[i] = x[i-1] + vx[i-1]*h + h*cm*x[i-1]/v[i-1];
		y[i] = y[i-1] + vy[i-1]*h + h*(-g*pow(h*i,2)*2 + cm*y[i-1]/v[i-1]);
	}**/
	//y[1] = y[0] + vy[0]*h + h*(-g*pow(h,2)/2 + cm*y[0]/v[0]);
	i = 1;
	while (y[i-1] >= 0.0){
		vx[i] = vx[i-1] + h*cm*vx[i-1]/v[i-1];
		vy[i] = vy[i-1] + h*(-g + cm*vy[i-1]/v[i-1]);
		v[i]=pow(((vx[i]*vx[i]) + (vy[i]*vy[i])) , 0.5);

		x[i] = x[i-1] + vx[i-1]*h + h*cm*x[i-1]/v[i-1];
		y[i] = y[i-1] + vy[i-1]*h + h*(-g*pow(h*i,2)*2 + cm*y[i-1]/v[i-1]);
		i = i + 1;
		
	
	}
		
	x[0]=0.0;
	y[0]=0.0;
	v[0]=300;
	vx[0]=v[0]*cos(40*pi/180); 
	vy[0]=vx[0]; 

	for (i=0; i<iter; i++){

		fprintf(posicion,"%f %f",x[i] ,y[i]);
		fprintf(posicion,"\n");

		fprintf(velocidadXY,"%f %f",vx[i] ,vy[i]);
		fprintf(velocidadXY,"\n");

		fprintf(MagnitudVelocidad,"%f %f", h*i ,v[i]);
		fprintf(MagnitudVelocidad,"\n");
	}
		
}

void rungekuta(double angulo, double *x, double *y, double *v, double *vx , double *vy){
			
	x[0]=0.0;
	y[0]=0.0;
	v[0]=300;
	vx[0]=v[0]*cos(angulo); 
	vy[0]=v[0]*sin(angulo); 

	//y[1] = y[0] + vy[0]*h + h*(-g*pow(h,2)/2 + cm*y[0]/v[0]);
	i=1;
	while (y[i-1] >= 0.0){
		vx[i] = vx[i-1] + h*cm*vx[i-1]/v[i-1];
		vy[i] = vy[i-1] + h*(-g + cm*vy[i-1]/v[i-1]);
		v[i]=pow(((vx[i]*vx[i]) + (vy[i]*vy[i])) , 0.5);

		x[i] = x[i-1] + vx[i-1]*h + h*cm*x[i-1]/v[i-1];
		y[i] = y[i-1] + vy[i-1]*h + h*(-g*pow(h*i,2)*2 + cm*y[i-1]/v[i-1]);
		i = i + 1;
	}
cout << "iteracion= "<< i << " ;" << angulo*180/pi  << endl;
cout << "         ultima posic"<< y[i+1] << " ;" << angulo*180/pi  << endl;

	x[0]=0.0;
	y[0]=0.0;
	v[0]=300;
	vx[0]=v[0]*cos(angulo); 
	vy[0]=v[0]*sin(angulo);	

}

void anularVectores(double *x, double *y, double *v, double *vx , double *vy){

	for (i=0; i<iter; i++){
		x[i]=0.0;
		y[i]=0.0;
		v[i]=0.0;
		vx[i]=0.0; 
		vy[i]=0.0;
	}
}
