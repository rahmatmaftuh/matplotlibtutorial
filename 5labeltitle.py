import numpy as np 
import matplotlib.pyplot as plt

#membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
	t = np.arange(0,tAkhir,0.1)
	y = amplitudo *np.sin(2*frekuensi*t+np.deg2rad(theta))
	return t,y

t,y = sinusGenerator(1,1,4,0)

#membuat plot
plt.plot(t,y)


#membuat label
judul = "Grafik Sinusoidal\n"
rumus = r"$ \mathcal{Y}=A.sin(2 \omega t + \theta)$" #buat nulis rumusnya coba pelajari nulis rumus matematika pake latex style
plt.title(judul + rumus)
plt.xlabel ("Waktu(detik)")
plt.ylabel("Amplitudo(meter)")

#menampilkan plot
plt.show()