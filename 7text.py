#kita bisa bikin text posisinya dimanapun
import numpy as np 
import matplotlib.pyplot as plt 


#membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
	t = np.arange(0,tAkhir,0.1)
	y = amplitudo *np.sin(2*frekuensi*t+np.deg2rad(theta))
	return t,y

#membuat plot
t,y = sinusGenerator(1,1,4,0)

plt.plot(t,y)
plt.text(1,1,"sin(90)")

#menampilkan plot
plt.show()