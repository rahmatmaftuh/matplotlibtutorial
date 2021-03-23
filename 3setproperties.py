#set properties intinya bisa nge custom lebih rinci gitu
import numpy as np 
import matplotlib.pyplot as plt 

#membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
	t = np.arange(0,tAkhir,0.1)
	y = amplitudo *np.sin(2*frekuensi*t+np.deg2rad(theta))
	return t,y

t1,y1 = sinusGenerator(1,1,4,0)
t2,y2 = sinusGenerator(1,1,4,30)
t3,y3 = sinusGenerator(1,1,4,90)
t4,y4 = sinusGenerator(1,1,4,100)

#membuat plot
dataPlot1 = plt.plot(t1,y1)
dataPlot2 = plt.plot(t2,y2)
dataPlot3 = plt.plot(t3,y3)
dataPlot4 = plt.plot(t4,y4)

#setting properties
#functionnya: plt.setp(plot,properties="nilai")
plt.setp(dataPlot1, color="r", linestyle="-", linewidth=2)
plt.setp(dataPlot2, color="b", linestyle="-.", linewidth=4)
plt.setp(dataPlot3, color="g", linestyle="-.", linewidth=8)
plt.setp(dataPlot4, color="y", linestyle="dotted", linewidth=10)
#supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

#menampilkan plot
plt.show()