import numpy as np
from fontTools.feaLib.ast import Statement
from Quaternions import  to_ssk
from Quaternions import quat_mult
from Quaternions import quat_sopr
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
A = 120
B = 120
C = 120
Iso=[1,0,0,0,1,0,0,0,1]
def GetOsk(Statement):
    OrbitalIso = np.zeros(9)
    R = Statement[:3]
    V = Statement[3:6]
    e1 = R / np.linalg.norm(R)
    RvecV = np.cross(R, V)
    e3 = RvecV / np.linalg.norm(RvecV)
    e2 = np.cross(e3, e1)
    OrbitalIso[:3] = e1
    OrbitalIso[3:6] = e2
    OrbitalIso[6:9] = e3
    return np.array([e1,e2,e3])
def getMatrix(Statement):
    State = np.array(Statement)
    Osk = GetOsk(State)
    A = np.zeros((3,3))
    e1=Iso[:3]
    e2=Iso[3:6]
    e3=Iso[6:9]
    e1_=Osk[0]
    e2_=Osk[1]
    e3_=Osk[2]
    A[:,0] = e1_
    A[:,1] = e2_
    A[:,2] = e3_
    return A

def matrix_to_quaternion(R):
    R = np.asarray(R, dtype=np.float64)
    trace = np.trace(R)

    if trace > 0:
        S = np.sqrt(trace + 1.0) * 2  # S = 4 * w
        w = 0.25 * S
        x = (R[2, 1] - R[1, 2]) / S
        y = (R[0, 2] - R[2, 0]) / S
        z = (R[1, 0] - R[0, 1]) / S
    elif R[0, 0] > R[1, 1] and R[0, 0] > R[2, 2]:
        S = np.sqrt(1.0 + R[0, 0] - R[1, 1] - R[2, 2]) * 2  # S = 4 * x
        w = (R[2, 1] - R[1, 2]) / S
        x = 0.25 * S
        y = (R[0, 1] + R[1, 0]) / S
        z = (R[0, 2] + R[2, 0]) / S
    elif R[1, 1] > R[2, 2]:
        S = np.sqrt(1.0 + R[1, 1] - R[0, 0] - R[2, 2]) * 2  # S = 4 * y
        w = (R[0, 2] - R[2, 0]) / S
        x = (R[0, 1] + R[1, 0]) / S
        y = 0.25 * S
        z = (R[1, 2] + R[2, 1]) / S
    else:
        S = np.sqrt(1.0 + R[2, 2] - R[0, 0] - R[1, 1]) * 2  # S = 4 * z
        w = (R[1, 0] - R[0, 1]) / S
        x = (R[0, 2] + R[2, 0]) / S
        y = (R[1, 2] + R[2, 1]) / S
        z = 0.25 * S

    return np.array([w, x, y, z])
def get_quat_relative(Statement):
    State = np.array(Statement)
    quat_new = matrix_to_quaternion(getMatrix(State))
    quat_sopr=np.array([quat_new[0],-1*quat_new[1],-1*quat_new[2],-1*quat_new[3]])
    quatotn = quat_mult( quat_sopr,State[9:13])
    return(quatotn)
A=[[np.sqrt(2)/2,-np.sqrt(2)/2,0],[np.sqrt(2)/2,np.sqrt(2)/2,0],[0,0,1]]
def getB(Statement):
    Bo= GetOsk(Statement)[2]
    Bgotov = to_ssk(Statement[9:13],Bo)
    return(Bgotov)
def getYakobi(Statement,A,B,C):
    Otn = to_ssk(Statement[9:13], Statement[0:3])
    BOtn = getB(Statement)
    part1=1/2*(A * (Statement[6]**2) + B * Statement[7]**2 + C * Statement[8]**2)
    part2 = 3/2*((Statement[6]**2 +  Statement[7]**2 +  Statement[8]**2)*(A* Otn[0]**2 + B*Otn[1] ** 2 + C *Otn[2]**2))
    part3 = -1 * ((Statement[6]**2 +  Statement[7]**2 +  Statement[8]**2)**(1/2))*(A*Statement[6]*BOtn[0] + B*Statement[7]*BOtn[1]+ B*Statement[8]*BOtn[2])
    Yakob = part1 + part2 + part3
    return Yakob
#print(to_ssk(initial_state[9:13],initial_state[0:3])[0])
#Otn = to_ssk(initial_state[9:13], initial_state[0:3])
#print(Otn)