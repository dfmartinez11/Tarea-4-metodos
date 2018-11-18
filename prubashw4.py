from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt("difusion.dat")
Ymax=50 
Xmax=50 
Tmax=30
dt=0.1

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
plt.title("Temperatura promedio transversal VS tiempo")			
plt.savefig("T_promedios.pdf")
plt.show()



#------------configuracion de equilibrio
estadoEnTiempo_t = datos[(Ymax*Xmax*29) : Ymax*Xmax*(30)]
T = estadoEnTiempo_t.transpose()[3]
	
plt.figure()	
x=np.linspace(0,50,50)
y=np.linspace(0,50,50)
X, Y = np.meshgrid(x, y)
	
t=np.ones((50,50))
for i in range(50):
	t[i]=T[(50*i) : 50*(i+1)]

tiempo = "Equilibrio en tiempo= "+ str(29*dt) + "s"
plt.contourf(X, Y, t,100, cmap=plt.cm.Spectral)
	
plt.title(tiempo)
cbar = plt.colorbar(plt.contourf(X, Y, t,10))
plt.savefig("Equilibrio.pdf")
plt.show()



#-----------para varios tiempos 2D
grafica=plt.figure()
for i in range(Tmax-20):

	estadoEnTiempo_t = datos[(Ymax*Xmax*i) : Ymax*Xmax*(i+1)]
	T = estadoEnTiempo_t.transpose()[3]
	
	ax = grafica.add_subplot(2, 5,1+i)
		
	x=np.linspace(0,50,50)
	y=np.linspace(0,50,50)
	X, Y = np.meshgrid(x, y)
	
	t=np.ones((50,50))
	for i in range(50):
		t[i]=T[(50*i) : 50*(i+1)]

	tiempo = "tiempo= "+ str(i*dt) + " s"
	ax.contourf(X, Y, t,100, cmap=plt.cm.Spectral)
	
	#ax.set_title(tiempo)
	cbar = plt.colorbar(plt.contourf(X, Y, t,10))
		
plt.savefig("difucion2D.pdf")
print " "
print "------Las graficas en 2D de la temperatura estan en difucion2D.pdf"


#------------para varios tiempos 3D
figura = plt.figure()
figura.suptitle('Evolucion de T con tiempo')
for i in range(Tmax-20):
	

	estadoEnTiempo_t = datos[(Ymax*Xmax*i) : Ymax*Xmax*(i+1)]
	x = estadoEnTiempo_t.transpose()[0]
	y = estadoEnTiempo_t.transpose()[1]
	T = estadoEnTiempo_t.transpose()[3]

	#axs[i] = figura.gca(projection='3d')

	ax1 = figura.add_subplot(2, 5,1+i, projection='3d')
	
	#ax1.scatter(x, y, T)
	#ax1.plot_wireframe(x, y, T)

	#axs[i].plot_trisurf(x, y, T, color ='w')-
	ax1.plot_trisurf(x, y, T, color ='w',  linewidth=0.2, cmap=plt.cm.Spectral)


	tiempo = "Temperatura en t= "+ str(i*dt) + " s"
	ax1.set_zlabel('temper.')
	ax1.text2D(0.05, 0.95, tiempo , transform=ax1.transAxes)

plt.savefig("difucion3D.pdf")
print "------Y las graficas en 3D ""animacion"" en difucion2D.pdf"	
plt.show()







	
	





