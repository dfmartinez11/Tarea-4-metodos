#include<iostream>
#include<cmath>
#include <stdio.h>
using namespace std;

#define Ymax 10000 //Esto es  100/0.01 = L/Dx
#define Tmax 3000
#define L 100
                        
main()
{
	double fut[Ymax], pres[Ymax] , pas[Ymax];
	int i, j ;

	double dt = 0.1;
	double dx = 0.1;
	double c = 2.0; //  esto es raiz(400/0.01)=raiz(T/ro)
	double D = dx/dt;
	//double n = c*c/(D*D);
	double n = 1.0;

	FILE *archivo;     
	archivo = fopen("difus.dat","w");
   
	//condiciones iniciales
	for(i=0; i<Ymax; i++){
		pas[i]=0.0; 
		if (i <= (0.8*L))	pres[i]=1.25*(-i/L);
		
		if (i > (0.8*L))	pres[i]=(5-5*(-i))/L;
	}

	pres[0]=0.0;        // bordes quietos
	pres[Ymax] =0.0;    // bordes quietos
      
	for(j=0; j<Tmax; j++) //3000*0.001 =3segundos
	{	   
		for(i=1; i<(Ymax-1); i++)                 
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

	printf("---los datos estan en difus.dat\n");
	fclose(archivo);

}
