import matplotlib.pyplot as plt
import math
import scipy
import numpy as np
from Equtaions import DiffState
from Quaternions import to_ssk
from OrbitalSo import get_quat_relative, getYakobi
from OrbitalSo import GetOsk
from OrbitalSo import getMatrix
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle, Arrow
from Quaternions import get_ssk_to_iso
Const = 3.986 * (10 ** 14)
A = 50
B = 100
C = 150
m = 100
x=1*7*(10**6)
y = 0
z = 0
Vx = 0
Vy=(Const/x)**(1/2)
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
Statements = np.zeros((2*60*600+1,13))
Statements[0] = initial_state
Wz = np.zeros(2*600*60+1)
Wz[0] = wz
time = np.arange(0,2*600*60+1,1)
Qotn = np.zeros((2*600*60+1,4))
X=[x]
Y=[y]
Qotn[0][:4]=[1,0.0001,0.0001,0.0001]
Yakob = np.zeros(2*600*60+1)
def Integrator(Vector, step):
    k1 = step * DiffState(Vector)
    k2 = step * DiffState(Vector + k1/2)
    k3 = step * DiffState(Vector+ k2/2)
    k4 = step * DiffState(Vector + k3)
    Next = Vector + (k1+2*k2+2*k3+k4)/6
    return Next
for i in range(2*600*60):
    curent_state = Statements[i]
    if i%300 == 0:
        q = curent_state[9:13]
        norm = np.linalg.norm(q)
        curent_state[9:13] = q / norm
    New_State = Integrator(curent_state, 1)
    Statements[i+1] = New_State
    Qotnnew = get_quat_relative(New_State)
    Qotn[i+1] = Qotnnew
    Wz[i+1]= New_State[8]
    #if i % 1570 == 0 :
        #print(GetOsk(New_State))
        #print()
        #print(get_ssk_to_iso(New_State))
    X.append(New_State[0])
    Y.append(New_State[1])
    Yakob[i+1] = getYakobi(New_State,A,B,C)
##data = np.column_stack(Statements)
##headers = ['x','y','z','Vx', 'Vy','Vz','wx','wy','wz','qx','qy','qz','qw']
##np.savetxt('data.txt', data,
           ##delimiter='\t',
           ##header='\t'.join(headers),
           ##fmt='%6d',
           ##comments='')
qx = Qotn[:,1:2]
qy = Qotn[:,2:3]
qz = Qotn[:,3:4]
def getStatements(Start):
    Statements = np.zeros((2 * 60 * 600 + 1, 13))
    Statements[0] = Start
    for i in range(2 * 600 * 60):
        curent_state = Statements[i]
        if i % 300 == 0:
            q = curent_state[9:13]
            norm = np.linalg.norm(q)
            curent_state[9:13] = q / norm
        New_State = Integrator(curent_state, 1)
        Statements[i + 1] = New_State
        Qotnnew = get_quat_relative(New_State)
        Qotn[i + 1] = Qotnnew
        Wz[i + 1] = New_State[8]
        return Statements
#plt.plot(time,qx,time,qy,time,qz)
plt.plot(time,Yakob)
plt.show()
