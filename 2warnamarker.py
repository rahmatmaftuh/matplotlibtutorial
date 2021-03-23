import numpy as np 
import matplotlib.pyplot as plt 

"""
1. membuat data
2. membuat plot
3. menampilkan plot
"""

# 1. membuat data (sin(2wt+theta))
# camel case = dia sinus huruf awalnya kecil, kalo class dia huruf S awalnya besar
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
	t = np.arange(0,tAkhir,0.1)
	y = amplitudo *np.sin(2*frekuensi*t+np.deg2rad(theta))
	return t,y
# 2. membuat plot
t1,y1 = sinusGenerator(1,1,4,0)
plt.plot(t1,y1)
t2,y2 = sinusGenerator(1,1,4,30)
plt.plot(t2,y2, 'g') #untuk merubah warna pada grafik. g disini maksudnya green, bisa diganti juga dengan blue, red, dll
t3,y3 = sinusGenerator(1,1,4,60)
plt.plot(t3,y3, 'b--') #ini marketnya jadi dia kaya garis putus2
t4,y4 = sinusGenerator(1,1,4,90)
plt.plot(t4,y4, 'v')


#3. menampilkan plot
plt.show()

#marker yang ada di matplotlib
# "."	point
# ","	pixel
# "o"	circle
# "v"	triangle_down
# "^"	triangle_up
# "<"	triangle_left
# ">"	triangle_right
# "1"	tri_down
# "2"	tri_up
# "3"	tri_left
# "4"	tri_right
# "8"	octagon
# "s"	square
# "p"	pentagon
# "P"	plus (filled)
# "s"	star
# "h"	hexagon1
# "H"	hexagon2
# "+"	plus
# "x"	x
# "X"	x (filled)
# "D"	diamond
# "d"	thin diamond
