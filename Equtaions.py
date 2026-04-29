import numpy as np
import math
from scipy.spatial.transform import Rotation as R
from Quaternions import quat_mult, to_ssk, DifQuat
Const = 3.986 * (10 ** 14)
A = 120
B = 120
C = 120


def Vdot(state_vector):
    r = state_vector[:3]
    r_norm = np.linalg.norm(r)
    acceleration = -Const * r / (r_norm ** 3)
    return acceleration


def Rdot(state_vector):
    return state_vector[3:6]


def Quatdot(state_vector):
    return DifQuat(state_vector[9:13], state_vector[6:9])


def Omegadot(state_vector):
    r=state_vector[:3]
    r_iso = r
    r_norm = np.linalg.norm(r)
    r_ssk=to_ssk(state_vector[9:13],r_iso)
    wx, wy, wz = state_vector[6:9]
    omega_1 = (C - B) * ((r_ssk[1] * r_ssk[2] * 3*Const / (r_norm ** 5)) - wz * wy)/A
    omega_2 = (A - C) * ((r_ssk[2] * r_ssk[0] * 3*Const / (r_norm ** 5)) - wx * wz)/B
    omega_3 = (B - A) * ((r_ssk[0] * r_ssk[1] * 3*Const / (r_norm ** 5)) - wy * wx)/C

    return np.array([omega_1, omega_2, omega_3])


def DiffState(state_vector):
    result = np.concatenate([
        Rdot(state_vector),
        Vdot(state_vector),
        Omegadot(state_vector),
        Quatdot(state_vector)
    ])
    return result