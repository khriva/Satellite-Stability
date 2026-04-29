import numpy as np
x=1*7*(10**6)
y = 0
z = 0
Vx = 0
Vy=(5/x)**(1/2)
Vz=0
wz=0.001
wx=0.0001
wy=0.0001
xy=0
qw=1
qx=0
qy=0
qz=0
initial_state = np.array([x, y, z, Vx, Vy, Vz, wx, wy, wz,qw, qx, qy, qz])
print(initial_state[0:3])