import numpy as np 
import matplotlib.pyplot as plt

"""
Langkah-langkah di matplotlib
1. Membuat data
2. Membuat plot
3. Menampilkan plot
"""

# 1. membuat data
x = np.array([1,2,3,4])
y = np.array([1,4,9,16])
y3 = np.array([3,12,27,48])

#membuat plot
plt.plot(x,y)
plt.plot(x,y3)

#menampilkan plot
plt.show()
