#show: 

	#display MagnitudVelocidad.pdf
difucion3D.pdf: prubashw4.py difusion.dat

	python prubashw4.py

difusion.dat: comp2 PDE.cpp

	g++ PDE.cpp -o comp2
	./comp2

MagnitudVelocidad.pdf: Plots_hw4.py MagnitudVelocidad.dat 

	python Plots_hw4.py

MagnitudVelocidad.dat: comp ODE.cpp

	g++ ODE.cpp -o comp
	./comp






