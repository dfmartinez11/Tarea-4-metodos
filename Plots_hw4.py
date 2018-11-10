#from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

a = plt.figure()
#ax1 = a.add_subplot(111,projection='3d')
lenn=10000
datos = np.loadtxt("difus.dat")

x = np.linspace(0,101,100)
y = np.linspace(0,101,100)


#ax1.plot_wireframe(x, y, z)
#x, y = np.meshgrid(x, y)

x=np.linspace(0,lenn,lenn)
print "len de y: ", len(datos[0:lenn])
print "len de x: ", len(x)

#plt.plot(x,datos[ 0 : lenn ])
#plt.plot(x,datos[ lenn : 2*lenn ])
#plt.plot(x,datos[ 2*lenn : 3*lenn ])

#-------No sirvio
#for i in range(0, 10001):
#	for j in range(1,10001):
#		plt.plot(x,datos[ i*10000 : j*10000 ])
#plt.show()

for i in range(0,14):
	plt.plot(x, datos[(i)*lenn : (i+1)*lenn])
plt.show()

