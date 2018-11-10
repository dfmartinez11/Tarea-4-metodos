###### Generar la figura Aleatorios.png
Armonico con Euler.png: graficasArmonico.py PosicionArmonicoEuler.txt

	python graficasArmonico.py 

Armonico con Euler.png: graficasArmonico.py PosicionArmonicoEuler.txt

	python graficasArmonico.py 

####### Ejecutar a.out
output.txt: a.out datos.cpp

	g++ datos.cpp -o a.out
	./a.out 

###### Abrir la figura
mostrar: 
	display Aleatorios.png

###### Borrar todos los archivos
clean:
	rm output.txt
rm Aleatorios.png
