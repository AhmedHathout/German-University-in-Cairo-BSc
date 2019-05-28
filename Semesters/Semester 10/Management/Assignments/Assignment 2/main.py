import matplotlib.pyplot as plt
import numpy as np

pv = np.linspace(0, 648000, 13)
ev = np.linspace(0, 127600, 3)
ac = np.linspace(0, 99200, 3)
bac = [12,648000]
eac = [10.15673981,503774.2947]

plt.plot(pv, linestyle='solid',label='PV')
plt.plot(ev, linestyle='dashed',label='EV')
plt.plot(ac, linestyle='dashdot',label='AC')
plt.scatter(bac[0],bac[1],label='BAC',color='red',marker='x')
plt.scatter(eac[0],eac[1],label='EAC',color='blue',marker='o')

plt.legend()

plt.show()
