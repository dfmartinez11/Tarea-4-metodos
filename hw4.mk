
hw4.pdf: hw4.tex Tpromedios.pdf 
	
	pdflatex hw4.tex  

Tpromedios.pdf: difusion3D.pdf

difusion3D.pdf: prubashw4.py difusion.dat

	python prubashw4.py

difusion.dat: comp2 PDE.cpp trayectoria.pdf

	g++ PDE.cpp -o comp2
	./comp2

trayectoria.pdf: MagnitudVelocidad.pdf

MagnitudVelocidad.pdf: Plots_hw4.py MagnitudVelocidad.dat 

	python Plots_hw4.py

MagnitudVelocidad.dat: comp ODE.cpp

	g++ ODE.cpp -o comp
	./comp










