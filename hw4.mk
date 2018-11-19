hw4.pdf: hw4.tex MagnitudVelocidad.pdf 
	
	pdflatex hw4.tex
	
	pdflatex hw4.tex
	gnome-open hw4.pdf  

MagnitudVelocidad.pdf: Plots_hw4.py MagnitudVelocidad.dat 

	python Plots_hw4.py

MagnitudVelocidad.dat: ODE.cpp difusion.dat

	g++ ODE.cpp -o comp
	./comp

difusion.dat: PDE.cpp 

	g++ PDE.cpp -o comp2
	./comp2









