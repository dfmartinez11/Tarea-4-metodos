#from mpl_toolkits.mplot3d import axes3d
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
plt.savefig("trayectoria.pdf")
#plt.show()


velocidad = np.loadtxt("velocidadXY.dat")
Mv = np.loadtxt("MagnitudVelocidad.dat")

#---Con esto garantizo que no aparezcan puntos de ceros como en velocidad y Mv

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

plt.subplot(1,2,1)
plt.plot( velocidadd.transpose()[0] , velocidadd.transpose()[1] , label="Vy vs Vx" , c="b")
plt.legend()
plt.subplot(1,2,2)
plt.plot( Mvv.transpose()[0],Mvv.transpose()[1] , label="|V| vs tiempo" , c="r")
plt.title("componentes y magnitud de V con angulo=40    ")
plt.savefig("Velocidad_40.pdf")
plt.legend()
#plt.show()

#----------------------------------------------------------------------------------------
datos = np.loadtxt("difusion.dat")



x = np.linspace(0,101,100)
y = np.linspace(0,101,100)

#ax1 = a.add_subplot(111,projection='3d')
#ax1.plot_wireframe(x, y, z)
#x, y = np.meshgrid(x, y)

x=np.linspace(0,lenn,lenn)
#print "len de y: ", len(datos[0:lenn])
#print "len de x: ", len(x)

#plt.plot(x,datos[ 0 : lenn ])
#plt.plot(x,datos[ lenn : 2*lenn ])
#plt.plot(x,datos[ 2*lenn : 3*lenn ])

#   No sirvio
#for i in range(0, 10001):
#	for j in range(1,10001):
#		plt.plot(x,datos[ i*10000 : j*10000 ])
#plt.show()


#---------------------------------------------------------------
#for i in range(0,14):
	#plt.plot(x, datos[(i)*lenn : (i+1)*lenn])
#plt.show()

