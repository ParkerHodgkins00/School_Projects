#Parker Hodgkins

import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

m = GEKKO()    # create GEKKO model
s = m.Param()  # speed of ethernet

p = m.Var(5.0)

m.Equation(p.dt()==(s*1000000000.0)/(p*8.0)) # df/dp = (speed * conversion)/(package size * conversion)
m.time = np.linspace(0,2000) # time points
print("Debug")
# solve ODEs and plot
m.options.IMODE = 4
m.options.TIME_SHIFT=0
print("Debug")

s.value = 1
m.solve(disp=False)
plt.plot(m.time,p,'r-',linewidth=2,label='s=1GB')

print("Debug")
s.value = 2
m.solve(disp=False)
plt.plot(m.time,p,'b-',linewidth=2,label='s=2GB')

print("Debug")
s.value = 0.5
m.solve(disp=False)
plt.plot(m.time,p,'g-',linewidth=2,label='s=500MB')

print("Debug")
s.value = 3
m.solve(disp=False)
plt.plot(m.time,p,'r--',linewidth=2,label='s=3GB')

print("Debug")
s.value = 4
m.solve(disp=False)
plt.plot(m.time,p,'b--',linewidth=2,label='s=4GB')

print("Debug")
s.value = 5
m.solve(disp=False)
plt.plot(m.time,p,'g--',linewidth=2,label='s=5GB')

print("Debug")
s.value = 6
m.solve(disp=False)
plt.plot(m.time,p,'r:',linewidth=2,label='s=6GB')

print("Debug")
plt.xlabel('# of packets')
plt.ylabel('F(p) Frames/number of packets')
plt.legend()
plt.show()