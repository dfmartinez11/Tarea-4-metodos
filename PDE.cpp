#include<iostream>
#include<cmath>
#include <stdio.h>
using namespace std;

#define Ymax 50
#define Xmax 50 //Esto es  50/1 = L/Dx
#define Tmax 30

int i, j , k, l;
double Cp = 820.0 / 1000.0 /273.15 ; //  J/g*C
double K = 1.62 *100.0 *100.0; //  cm*cm/s
double p = 2.71; //  g/(cm*cm*cm)
double nu = K/(Cp*p);

//barilla de 10cm con 100C   
                        
int main()
{
	cout << "nu =" << nu << endl;	
	double pres[Xmax][Ymax] , fut[Xmax][Ymax]; // pres=presente , fut=futuro
	double dt = 0.1; 
	double dx = 1.0; // tomamos cambios dx, dy como iguales
		
	FILE *archivo;     
	archivo = fopen("difusion.dat","w");


   	for(j=0; j < Ymax; j++){		//condiciones iniciales generales
		for(i=0; i < Xmax; i++){
			pres[i][j]=0.0; 
		}
	}
		
			
	for(k=0 ; k<Tmax ; k++){ 
		//cout << "  " << k*dt<< endl;

		/*for(j=0; 23 <= j <=27; j++){		//condiciones de borde con barilla----------------
			for(i=0; 20 <= i <= 30; i++){
				pres[i][j]=100.0; 
			}
		}**/	
		pres[23][23]=100.0;	//inicializo directamente debido a un SEGMENTATION FAULT
		pres[23][24]=100.0;
		pres[23][25]=100.0;
		pres[23][26]=100.0;
		pres[24][23]=100.0;
		pres[24][24]=100.0;
		pres[24][25]=100.0;
		pres[24][26]=100.0;
		pres[25][23]=100.0;
		pres[25][24]=100.0;
		pres[25][25]=100.0;
		pres[25][26]=100.0;
		pres[26][24]=100.0;
		pres[26][23]=100.0;
		pres[26][25]=100.0;
		pres[26][26]=100.0;

		//condiciones de borde exterior 10C
		for(l=0; l < Xmax; l++){
			pres[0][l]=10.0;
			pres[49][l]=10.0;
			pres[l][0]=10.0;
			pres[l][49]=10.0;
		}

		for(i=1 ; i<Xmax ; i++){

			for(j=1 ; j<Ymax ; j++){

				// (dt*nu/(dx*dx)) =1

				fut[i][j] = pres[i][j] + (nu*dt/pow(dt,2)) *(-4*pres[i][j] + pres[i+1][j] + pres[i-1][j] + pres[i][j+1] + pres[i][j-1]);
				/*fut[23][23]=100.0;// RE - inicializo directamente 
				fut[23][24]=100.0;
				fut[23][25]=100.0;
				fut[23][26]=100.0;
				fut[24][23]=100.0;
				fut[24][24]=100.0;
				fut[24][25]=100.0;
				fut[24][26]=100.0;
				fut[25][23]=100.0;
				fut[25][24]=100.0;
				fut[25][25]=100.0;
				fut[25][26]=100.0;
				fut[26][24]=100.0;
				fut[26][23]=100.0;
				fut[26][25]=100.0;
				fut[26][26]=100.0;

				for(l=0; l < Xmax; l++){
					fut[0][l]=10.0;
					fut[49][l]=10.0;
					fut[l][0]=10.0;
					fut[l][49]=10.0;
				}

				fprintf(archivo, "%f %f %f %f \n", i*dx , j*dx , k*dt , pres[i-1][j]);
				//cout <<  i*dx << " " << j*dx <<" " << k*dt <<" " << pres[i][j] << endl;
				pres[i-1][j] = fut[i-1][j];    **/	
							
			}
					

			for(j=0 ; j<Ymax ; j++){
				fut[23][23]=100.0;// RE - inicializo directamente 
				fut[23][24]=100.0;
				fut[23][25]=100.0;
				fut[23][26]=100.0;
				fut[24][23]=100.0;
				fut[24][24]=100.0;
				fut[24][25]=100.0;
				fut[24][26]=100.0;
				fut[25][23]=100.0;
				fut[25][24]=100.0;
				fut[25][25]=100.0;
				fut[25][26]=100.0;
				fut[26][24]=100.0;
				fut[26][23]=100.0;
				fut[26][25]=100.0;
				fut[26][26]=100.0;

				for(l=0; l < Xmax; l++){
					fut[0][l]=10.0;
					fut[49][l]=10.0;
					fut[l][0]=10.0;
					fut[l][49]=10.0;
				}
	
				if(fut[i-1][j] > 100.0)	fut[i-1][j] = 100.0;  //condicion de equilibrio hasta 100C
				if(fut[i-1][j] < 0.0)	fut[i-1][j] = 0.0;  //condicion de minimo de temp. en 0.0C

				fprintf(archivo, "%f %f %f %f \n", (i-1)*dx , j*dx , k*dt , pres[i-1][j]);
				//cout <<  (i-1)*dx << " " << j*dx <<" " << k*dt <<" " << pres[i][j] << endl;
				pres[i-1][j] = fut[i-1][j];
				/*  fprintf(archivo, "%f %f %f %f \n", (49)*dx , l*dx , k*dt , pres[49][j]);
				pres[49][j] = fut[49][j];  **/	
			}
			/* fprintf(archivo, "%f %f %f %f \n", (49)*dx , l*dx , k*dt , pres[49][i]);
			pres[49][i] = fut[49][i]; **/
		}
		for(l=0; l < Xmax; l++){ 
			fprintf(archivo, "%f %f %f %f \n", (49)*dx , l*dx , k*dt , pres[49][l]);
			pres[49][j] = fut[49][j];  
		}   
			
	}

	cout << "se completo el procedimiento, felicidades, jaja" << endl;

	return 0;
}
