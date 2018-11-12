#include<iostream>
#include<cmath>
#include <stdio.h>
using namespace std;

#define Ymax 4
#define Xmax 4 //Esto es  50/1 = L/Dx
#define Tmax 1

int i, j , k;
double Cp = 820.0 / 1000.0 ; //  J/g*K
double K = 1.62 *100.0 *100.0; //  cm*cm/s
double p = 2.71; //  g/(cm*cm*cm)
double nu = K/(Cp*p);

//barilla de 10cm con 100C = 373.15K  
                        
int main()
{
	cout << "nu =" << nu << endl;	
	double pres[Xmax][Ymax] , fut[Xmax][Ymax];
	double dt = 0.1;
	double dx = 1.0; //tomamos cambios dx, dy como iguales
		
	FILE *archivo;     
	archivo = fopen("difusion.dat","w");
   
	for(j=0; j < Ymax; j++){
		for(i=0; i < Xmax; i++){
			pres[i][j]=293.15; 
		}
	}
	//condiciones de borde con barilla
	/*
	for(j=0; 2 <= j <=3; j++){
		for(i=0; 2 <= i <= 3; i++){
			pres[i][j]=373.15; 
		}
	}
	**/
	
	//condiciones de borde 10C
	for(i=0; i < 4; i++){
		pres[0][i]=283.15;
		pres[i][0]=283.15;
		pres[i][3]=283.15;
		pres[3][i]=283.15;
	}

	
	for(k=0 ; k<Tmax ; k++){ 
		//cout << "  " << k*dt<< endl;
		for(i=1 ; k<Xmax ; i++){
			for(j=1 ; k<Ymax ; j++){
				fut[i][j] = pres[i][j] + (dt*10/(dx*dx))*(-4*pres[i][j] + pres[i+1][j] + pres[i-1][j] + pres[i][j+1] + pres[i][j-1]);
				fprintf(archivo, "%f %f %f %f", i*dx , j*dx , k*dt , pres[i][j]);
				cout <<  i*dx << " " << j*dx <<" " << k*dt <<" " << pres[i][j] << endl;
				pres[i][j] = fut[i][j];
				
			}
			fprintf(archivo, "\n");	
		}
		fprintf(archivo, "\n");	
		/*for(i=1 ; k<Xmax ; i++){
			for(j=1 ; k<Ymax ; j++){
				fprintf(archivo, "%f %f %f", i*dx , j*dx , k*dt );
				pres[i][j] = fut[i][j];
			}
		}**/		
	}
	cout << "se completo el procedimiento" << endl;

/*
	for(j=0; j<Tmax; j++) //3000*0.001 =3segundos
	{	   
		for(i=1; i<Ymax; i++)                 
      		{

      			fut[i] = (2*pres[i])-pas[i] +0.5*(pres[i+1] + pres[i-1] - (2*pres[i]));
      		}

      		for(i=1; i<(Ymax-1); i++)                 
      		{
			if(j%200 == 0)	fprintf(archivo, "%f\n" , pres[i]);
			pas[i] = pres[i];
			pres[i]= fut[i];

      		}
        	//if(j%200 == 0) fprintf(output, "\n");
	}

	printf("---los datos estan en difusion.dat\n");
	fclose(archivo);
**/
	return 0;
}
