from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


#--------------------------------------------------------------
#datos = np.loadtxt("difus.dat")
#posicion = np.loadtxt("posicion.dat")
#posicion10 = np.loadtxt("10_posicion.dat")
#posicion20 = np.loadtxt("20_posicion.dat")
#posicion30 = np.loadtxt("30_posicion.dat")
#posicion50 = np.loadtxt("50_posicion.dat")
#posicion60 = np.loadtxt("60_posicion.dat")
#posicion70 = np.loadtxt("70_posicion.dat")
#plt.plot(posicion.transpose()[0],posicion.transpose()[1])
#plt.plot(posicion10.transpose()[0],posicion10.transpose()[1])
#plt.plot(posicion20.transpose()[0],posicion20.transpose()[1])
#plt.plot(posicion30.transpose()[0],posicion30.transpose()[1])
#plt.plot(posicion50.transpose()[0],posicion50.transpose()[1])
#plt.plot(posicion60.transpose()[0],posicion60.transpose()[1])
#plt.plot(posicion70.transpose()[0],posicion70.transpose()[1])
#plt.title("posicion, Y vs X para diferentes angulos")
#plt.savefig("trayectoria.pdf")

#plt.show()
#----------------------------------------------------------------------------------------
datos = np.loadtxt("difusion.dat")
Ymax=50 
Xmax=50 
Tmax=10
dt=0.1

#estadoEnTiempo_t = datos[0 : Ymax*Xmax]
#x = estadoEnTiempo_t.transpose()
#print x

estadoEnTiempo_t = datos[0 : Ymax*Xmax]
x = estadoEnTiempo_t.transpose()[0]
y = estadoEnTiempo_t.transpose()[1]
T = estadoEnTiempo_t.transpose()[3]
print x[0], " ", T[0]
print x[-1], " ", T[-1]
estadoEnTiempo_t = datos[(Ymax*Xmax) : Ymax*Xmax*(2)]
x = estadoEnTiempo_t.transpose()[0]
y = estadoEnTiempo_t.transpose()[1]
T = estadoEnTiempo_t.transpose()[3]
print x[0], " ", T[0]
print x[-1], " ", T[-1]



for i in range(Tmax):

	#print datos[(Ymax*Xmax*i) : Ymax*Xmax*(i+1)]
	#print " "

	estadoEnTiempo_t = datos[(Ymax*Xmax*i) : Ymax*Xmax*(i+1)]
	x = estadoEnTiempo_t.transpose()[0]
	y = estadoEnTiempo_t.transpose()[1]
	T = estadoEnTiempo_t.transpose()[3]

	#print x ," ", y ," ", T
	#print " "

	a = plt.figure()
	ax1 = a.add_subplot(111,projection='3d')
	ax1.plot_wireframe(x, y, T)
	
	tiempo = "Temperatura en t= "+str(i*dt)+" s"
	plt.xlabel("POSICION X")
	plt.ylabel("POSICION Y")
	#---no existe zlabel----plt.zlabel("Temeperatura (K)")
	plt.title(tiempo)
	plt.show()
	#x, y = np.meshgrid(x, y)

#print "--------t=0.0"
#print datos[0:Ymax*Xmax]
#print " "
#print "--------t=0.1"
#print datos[Ymax*Xmax:Ymax*Xmax*2]
#print " "




