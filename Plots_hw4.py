from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

#a = plt.figure()
lenn=10000

plt.figure()
#------------------------------------------------------------------------------------------
posicion = np.loadtxt( "posicion.dat" )
posicion10 = np.loadtxt( "10_posicion.dat" )
posicion20 = np.loadtxt( "20_posicion.dat" )
posicion30 = np.loadtxt( "30_posicion.dat" )
posicion50 = np.loadtxt( "50_posicion.dat" )
posicion60 = np.loadtxt( "60_posicion.dat" )
posicion70 = np.loadtxt( "70_posicion.dat" )


plt.plot( posicion10.transpose()[0] , posicion10.transpose()[1] , label="10" )
plt.plot( posicion20.transpose()[0] , posicion20.transpose()[1] , label="20" )
plt.plot( posicion30.transpose()[0] , posicion30.transpose()[1] , label="30" )
plt.plot( posicion.transpose()[0] ,posicion.transpose()[1] , label="40--" )
plt.plot( posicion50.transpose()[0] , posicion50.transpose()[1] , label="50" )
plt.plot( posicion60.transpose()[0] , posicion60.transpose()[1] , label="60" )
plt.plot( posicion70.transpose()[0] , posicion70.transpose()[1] , label="70" )

plt.legend()
plt.title("posicion, Y vs X para diferentes angulos")
plt.savefig("trayectoria.png")
#plt.show()


velocidad = np.loadtxt("velocidadXY.dat")
Mv = np.loadtxt("MagnitudVelocidad.dat")

#-Con esto garantizo que no aparezcan puntos de ceros como en velocidad y Mv

n=0
for i in range(1, velocidad.shape[0]):
	if (velocidad[i].all() != 0.0):
		n += 1

velocidadd = np.ones((n+1,2))
for i in range(n+1):
	velocidadd[i]=velocidad[i]


k=0
for i in range(1, Mv.shape[0]):
	if (velocidad[i].all() != 0.0):
		k += 1

Mvv = np.ones((k+1,2))
for i in range(k+1):
	Mvv[i]=Mv[i]

figura=plt.figure()
plt.title("componentes y magnitud de V con angulo=40")
ax1 = figura.add_subplot(1,2,1)
ax1.plot( velocidadd.transpose()[0] , velocidadd.transpose()[1] , label="Vy vs Vx, 40 grados" , c="b")
plt.legend()
ax2 = figura.add_subplot(1,2,2)
ax2.plot( Mvv.transpose()[0],Mvv.transpose()[1] , label="|V| vs tiempo, 40 grados" , c="r")
plt.legend()
#plt.title("componentes y magnitud de V con angulo=40    ")
plt.savefig("Velocidad_40.png")
#plt.show()


#----------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------
#--------------------------------------------------------- condiciones fontera PERIODICAS
Ymax=50 
Xmax=50 
Tmax=50
dt=0.1

datos = np.loadtxt("difusionPeriodicas.dat")

#-----------promedios de T
tiempo = []
temperaturaP = []
graf = plt.figure()
for k in range(Tmax):

	estadoEnTiempo_t = datos[(Ymax*Xmax*k) : Ymax*Xmax*(k+1)]
	T = estadoEnTiempo_t.transpose()[3]
	promedio=T.mean()
	#print promedio
	tiempo.append(k*dt)
	temperaturaP.append(promedio)

plt.plot(tiempo, temperaturaP, c="g")
plt.title("Temperatura promedio VS tiempo hasta 5s con fronteras Periodicas")			
plt.savefig("T_promediosPeriodicas.png")
#plt.show()



#------------configuracion de equilibrio
estadoEnTiempo_t = datos[(Ymax*Xmax*49) : Ymax*Xmax*(50)]
T = estadoEnTiempo_t.transpose()[3]
	
grafica = plt.figure()
ax = grafica.add_subplot(1, 2, 1)	
x=np.linspace(0,50,50)
y=np.linspace(0,50,50)
X, Y = np.meshgrid(x, y)

	
t=np.ones((50,50))
for i in range(50):
	t[i]=T[(50*i) : 50*(i+1)]


tiempo = "Equilibrio en tiempo= "+ str(49*dt) + "s con Periodicas"
ax.contourf(X, Y, t,100,  colors="b")
cbar = plt.colorbar(plt.contourf(X, Y, t,10))

x = estadoEnTiempo_t.transpose()[0]
y = estadoEnTiempo_t.transpose()[1]
ax2 = grafica.add_subplot(1, 2, 2, projection='3d')
ax2.plot_trisurf(x, y, T, color ='w',  linewidth=0.2 , cmap=plt.cm.PuBu_r)

plt.title(tiempo)
plt.savefig("EquilibrioPeriodicas.png")
#plt.show()



#-----------para varios tiempos 2D
grafica=plt.figure()
grafica.suptitle('Evolucion de T Periodicas con tiempo hasta 3s')
for i in range(Tmax-40):
	if (i!=3 and i!=7):
		estadoEnTiempo_t = datos[(Ymax*Xmax*i) : Ymax*Xmax*(i+1)]
		T = estadoEnTiempo_t.transpose()[3]
		if (i==0):
			ax = grafica.add_subplot(2, 4,1)
		if (i==1):
			ax = grafica.add_subplot(2, 4,2)
		if (i==2):
			ax = grafica.add_subplot(2, 4,3)
		if (i==4):
			ax = grafica.add_subplot(2, 4,4)
		if (i==5):
			ax = grafica.add_subplot(2, 4,5)
		if (i==6):
			ax = grafica.add_subplot(2, 4,6)
		if (i==8):
			ax = grafica.add_subplot(2, 4,7)
		if (i==9):
			ax = grafica.add_subplot(2, 4,8)
		x=np.linspace(0,50,50)
		y=np.linspace(0,50,50)
		X, Y = np.meshgrid(x, y)
	
		t=np.ones((50,50))
		for i in range(50):
			t[i]=T[(50*i) : 50*(i+1)]

		tiempo = "tiempo= "+ str(i*dt) + " s"
		ax.contourf(X, Y, t,100,  colors="b")
	
		ax.set_title(tiempo)
		cbar = plt.colorbar(plt.contourf(X, Y, t,10))
		
plt.savefig("difusion2DPeriodicas.png")
#plt.show()
print (" ")
print ("------Las graficas en 2D condiciones Periodicas de la temperatura estan en difucion2DPeriodicas.png y analogamente para 3D")


#------------para varios tiempos 3D
figura = plt.figure()
figura.suptitle('Evolucion de T Periodicas con tiempo hasta 3s')
for i in range(Tmax-40):
	
	if (i!=3 and i!=7):

		estadoEnTiempo_t = datos[(Ymax*Xmax*i) : Ymax*Xmax*(i+1)]
		x = estadoEnTiempo_t.transpose()[0]
		y = estadoEnTiempo_t.transpose()[1]
		T = estadoEnTiempo_t.transpose()[3]
		if(i==0): 
			ax1 = figura.add_subplot(2, 4,1, projection='3d')
		if(i==1): 
			ax1 = figura.add_subplot(2, 4,2, projection='3d')
		if(i==2): 
			ax1 = figura.add_subplot(2, 4,3, projection='3d')
		if(i==4): 
			ax1 = figura.add_subplot(2, 4,4, projection='3d')
		if(i==5): 
			ax1 = figura.add_subplot(2, 4,5, projection='3d')
		if(i==6): 
			ax1 = figura.add_subplot(2, 4,6, projection='3d')
	
		if(i==8): 
			ax1 = figura.add_subplot(2, 4,7, projection='3d')
		if(i==9): 
			ax1 = figura.add_subplot(2, 4,8, projection='3d')
		#ax1.plot_wireframe(x, y, T)

		#axs[i].plot_trisurf(x, y, T, color ='w')-
		ax1.plot_trisurf(x, y, T, color ='w',  linewidth=0.2, cmap=plt.cm.PuBu_r)


		tiempo = "t= "+ str(i*dt) 
		#ax1.set_zlabel('temper.')
		ax1.text2D(0.05, 0.95, tiempo)

plt.savefig("difusion3DPeriodicas.png")
print ("----")	
#plt.show()


#---------------------------------------------------------------------------------------------------------
#--------------------------------------------------------- condiciones fontera CERRADAS
#-----------promedios de T
datos = np.loadtxt("difusion.dat")
tiempo = []
temperaturaP = []
graf = plt.figure()
for k in range(Tmax):

	estadoEnTiempo_t = datos[(Ymax*Xmax*k) : Ymax*Xmax*(k+1)]
	T = estadoEnTiempo_t.transpose()[3]
	promedio=T.mean()
	#print promedio
	tiempo.append(k*dt)
	temperaturaP.append(promedio)

plt.plot(tiempo, temperaturaP)
plt.title("Temperatura promedio VS tiempo hasta 5s, fronteras cerradas")			
plt.savefig("T_promedios.png")
#plt.show()



#------------configuracion de equilibrio
estadoEnTiempo_t = datos[(Ymax*Xmax*49) : Ymax*Xmax*(50)]
T = estadoEnTiempo_t.transpose()[3]
	
grafica = plt.figure()
ax = grafica.add_subplot(1, 2, 1)	
x=np.linspace(0,50,50)
y=np.linspace(0,50,50)
X, Y = np.meshgrid(x, y)

	
t=np.ones((50,50))
for i in range(50):
	t[i]=T[(50*i) : 50*(i+1)]


tiempo = "Equilibrio en tiempo= "+ str(49*dt) + "s con Cerradas"
ax.contourf(X, Y, t,100, cmap=plt.cm.Spectral)
cbar = plt.colorbar(plt.contourf(X, Y, t,10))

x = estadoEnTiempo_t.transpose()[0]
y = estadoEnTiempo_t.transpose()[1]
ax2 = grafica.add_subplot(1, 2, 2, projection='3d')
ax2.plot_trisurf(x, y, T, color ='w',  linewidth=0.2, cmap=plt.cm.Spectral)

plt.title(tiempo)
plt.savefig("Equilibrio.png")
#plt.show()



#-----------para varios tiempos 2D
grafica=plt.figure()
grafica.suptitle('Evolucion de T Cerrada con tiempo hasta 3s')
for i in range(Tmax-40):
	if (i!=3 and i!=7):
		estadoEnTiempo_t = datos[(Ymax*Xmax*i) : Ymax*Xmax*(i+1)]
		T = estadoEnTiempo_t.transpose()[3]
		
		if (i==0):
			ax = grafica.add_subplot(2, 4,1)
		if (i==1):
			ax = grafica.add_subplot(2, 4,2)
		if (i==2):
			ax = grafica.add_subplot(2, 4,3)
		if (i==4):
			ax = grafica.add_subplot(2, 4,4)
		if (i==5):
			ax = grafica.add_subplot(2, 4,5)
		if (i==6):
			ax = grafica.add_subplot(2, 4,6)
		if (i==8):
			ax = grafica.add_subplot(2, 4,7)
		if (i==9):
			ax = grafica.add_subplot(2, 4,8)
		
		x=np.linspace(0,50,50)
		y=np.linspace(0,50,50)
		X, Y = np.meshgrid(x, y)
	
		t=np.ones((50,50))
		for i in range(50):
			t[i]=T[(50*i) : 50*(i+1)]

		tiempo = "tiempo= "+ str(i*dt) + " s"
		ax.contourf(X, Y, t,100, cmap=plt.cm.Spectral)
	
		ax.set_title(tiempo)
		cbar = plt.colorbar(plt.contourf(X, Y, t,10))
		
plt.savefig("difusion2D.png")
#plt.show()
print (" ")
print ("------Las graficas en 2D de la temperatura estan en difucion2D.png")


#------------para varios tiempos 3D
figura = plt.figure()
figura.suptitle('Evolucion de T Cerrada con tiempo hasta 3s')
for i in range(Tmax-40):
	
	if (i!=3 and i!=7):
		estadoEnTiempo_t = datos[(Ymax*Xmax*i) : Ymax*Xmax*(i+1)]
		x = estadoEnTiempo_t.transpose()[0]
		y = estadoEnTiempo_t.transpose()[1]
		T = estadoEnTiempo_t.transpose()[3]

		if(i==0): 
			ax1 = figura.add_subplot(2, 4,1, projection='3d')
		if(i==1): 
			ax1 = figura.add_subplot(2, 4,2, projection='3d')
		if(i==2): 
			ax1 = figura.add_subplot(2, 4,3, projection='3d')
		if(i==4): 
			ax1 = figura.add_subplot(2, 4,4, projection='3d')
		if(i==5): 
			ax1 = figura.add_subplot(2, 4,5, projection='3d')
		if(i==6): 
			ax1 = figura.add_subplot(2, 4,6, projection='3d')
	
		if(i==8): 
			ax1 = figura.add_subplot(2, 4,7, projection='3d')
		if(i==9): 
			ax1 = figura.add_subplot(2, 4,8, projection='3d')
		
		#ax1.plot_wireframe(x, y, T)

		#axs[i].plot_trisurf(x, y, T, color ='w')-
		ax1.plot_trisurf(x, y, T, color ='w',  linewidth=0.2, cmap=plt.cm.Spectral)


		tiempo = "t= "+ str(i*dt) 
		#ax1.set_zlabel('temper.')
		ax1.text2D(0.05, 0.95, tiempo)

plt.savefig("difusion3D.png")
print ("------Y las graficas en 3D ""animacion"" en difucion2D.png")	
#plt.show()



#---------------------------------------------------------------------------------------------------------
#--------------------------------------------------------- condiciones fontera abiertas

datos = np.loadtxt("difusionAbiertas.dat")

#-----------promedios de T
tiempo = []
temperaturaP = []
graf = plt.figure()
for k in range(Tmax):

	estadoEnTiempo_t = datos[(Ymax*Xmax*k) : Ymax*Xmax*(k+1)]
	T = estadoEnTiempo_t.transpose()[3]
	promedio=T.mean()
	#print promedio
	tiempo.append(k*dt)
	temperaturaP.append(promedio)

plt.plot(tiempo, temperaturaP, c="r")
plt.title("Temperatura promedio VS tiempo hasta 5s con fronteras Abiertas")			
plt.savefig("T_promediosAbiertas.png")
#plt.show()



#------------configuracion de equilibrio
estadoEnTiempo_t = datos[(Ymax*Xmax*49) : Ymax*Xmax*(50)]
T = estadoEnTiempo_t.transpose()[3]
	
grafica = plt.figure()
ax = grafica.add_subplot(1, 2, 1)	
x=np.linspace(0,50,50)
y=np.linspace(0,50,50)
X, Y = np.meshgrid(x, y)

	
t=np.ones((50,50))
for i in range(50):
	t[i]=T[(50*i) : 50*(i+1)]


tiempo = "Equilibrio en tiempo= "+ str(49*dt) + "s con Abiertas"
ax.contourf(X, Y, t,100, cmap=plt.cm.Spectral)
cbar = plt.colorbar(plt.contourf(X, Y, t,10))

x = estadoEnTiempo_t.transpose()[0]
y = estadoEnTiempo_t.transpose()[1]
ax2 = grafica.add_subplot(1, 2, 2, projection='3d')
ax2.plot_trisurf(x, y, T, color ='w',  linewidth=0.2)

plt.title(tiempo)
plt.savefig("EquilibrioAbiertas.png")
#plt.show()



#-----------para varios tiempos 2D
grafica=plt.figure()
grafica.suptitle('Evolucion de T Abierta con tiempo hasta 3s')
for i in range(Tmax-40):
	if (i!=3 and i!=7):
		estadoEnTiempo_t = datos[(Ymax*Xmax*i) : Ymax*Xmax*(i+1)]
		T = estadoEnTiempo_t.transpose()[3]
		if (i==0):
			ax = grafica.add_subplot(2, 4,1)
		if (i==1):
			ax = grafica.add_subplot(2, 4,2)
		if (i==2):
			ax = grafica.add_subplot(2, 4,3)
		if (i==4):
			ax = grafica.add_subplot(2, 4,4)
		if (i==5):
			ax = grafica.add_subplot(2, 4,5)
		if (i==6):
			ax = grafica.add_subplot(2, 4,6)
		if (i==8):
			ax = grafica.add_subplot(2, 4,7)
		if (i==9):
			ax = grafica.add_subplot(2, 4,8)
		x=np.linspace(0,50,50)
		y=np.linspace(0,50,50)
		X, Y = np.meshgrid(x, y)
	
		t=np.ones((50,50))
		for i in range(50):
			t[i]=T[(50*i) : 50*(i+1)]

		tiempo = "tiempo= "+ str(i*dt) + " s"
		ax.contourf(X, Y, t,100, cmap=plt.cm.Spectral)
	
		ax.set_title(tiempo)
		cbar = plt.colorbar(plt.contourf(X, Y, t,10))
		
plt.savefig("difusion2DAbiertas.png")
#plt.show()
print (" ")
print ("------Las graficas en 2D condiciones Abiertas de la temperatura estan en difucion2DAbiertas.png y de manera analoga para 3D")
print (" ")


#------------para varios tiempos 3D
figura = plt.figure()
figura.suptitle('Evolucion de T Abierta con tiempo hasta 3s')
for i in range(Tmax-40):
	
	if (i!=3 and i!=7):

		estadoEnTiempo_t = datos[(Ymax*Xmax*i) : Ymax*Xmax*(i+1)]
		x = estadoEnTiempo_t.transpose()[0]
		y = estadoEnTiempo_t.transpose()[1]
		T = estadoEnTiempo_t.transpose()[3]
		if(i==0): 
			ax1 = figura.add_subplot(2, 4,1, projection='3d')
		if(i==1): 
			ax1 = figura.add_subplot(2, 4,2, projection='3d')
		if(i==2): 
			ax1 = figura.add_subplot(2, 4,3, projection='3d')
		if(i==4): 
			ax1 = figura.add_subplot(2, 4,4, projection='3d')
		if(i==5): 
			ax1 = figura.add_subplot(2, 4,5, projection='3d')
		if(i==6): 
			ax1 = figura.add_subplot(2, 4,6, projection='3d')
	
		if(i==8): 
			ax1 = figura.add_subplot(2, 4,7, projection='3d')
		if(i==9): 
			ax1 = figura.add_subplot(2, 4,8, projection='3d')
		#ax1.plot_wireframe(x, y, T)

		#axs[i].plot_trisurf(x, y, T, color ='w')-
		ax1.plot_trisurf(x, y, T, color ='w',  linewidth=0.2)


		tiempo = "t= "+ str(i*dt) 
		#ax1.set_zlabel('temper.')
		ax1.text2D(0.05, 0.95, tiempo)

plt.savefig("difusion3DAbiertas.png")
	
#plt.show()

