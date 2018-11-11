#from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

a = plt.figure()
lenn=10000

plt.figure()
#--------------------------------------------------------------
#datos = np.loadtxt("difus.dat")
posicion = np.loadtxt("posicion.dat")
posicion10 = np.loadtxt("10_posicion.dat")
posicion20 = np.loadtxt("20_posicion.dat")
posicion30 = np.loadtxt("30_posicion.dat")
posicion50 = np.loadtxt("50_posicion.dat")
posicion60 = np.loadtxt("60_posicion.dat")
posicion70 = np.loadtxt("70_posicion.dat")

plt.plot(posicion.transpose()[0],posicion.transpose()[1])
plt.plot(posicion10.transpose()[0],posicion10.transpose()[1])
plt.plot(posicion20.transpose()[0],posicion20.transpose()[1])
plt.plot(posicion30.transpose()[0],posicion30.transpose()[1])
plt.plot(posicion50.transpose()[0],posicion50.transpose()[1])
plt.plot(posicion60.transpose()[0],posicion60.transpose()[1])
plt.plot(posicion70.transpose()[0],posicion70.transpose()[1])
plt.title("posicion, Y vs X para diferentes angulos")
plt.savefig("trayectoria.pdf")

plt.show()

velocidad = np.loadtxt("velocidadXY.dat")
plt.plot(velocidad.transpose()[0],velocidad.transpose()[1])
plt.title("velocidad_X vs velocidad_Y")
plt.savefig("velX vs velY.pdf")
plt.show()

Mv = np.loadtxt("MagnitudVelocidad.dat")
plt.plot(Mv.transpose()[0],Mv.transpose()[1])
plt.title("magnitud velocidad Vs tiempo")
plt.savefig("magnitud velocidad.pdf")
plt.show()




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

