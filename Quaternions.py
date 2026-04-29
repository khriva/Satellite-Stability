import numpy as np
def quat_mult(q1, q2):
    "Формат: [w, x, y, z]"

    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2

    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
    z = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2

    return np.array([w, x, y, z])
def quat_sopr(q):
    return np.array([q[0],-q[1],-q[2],-q[3]])
def to_ssk(q,v):
    vx,vy,vz = v
    q0,q1,q2,q3= q
    p_iso = [0,vx,vy,vz]
    q_inv = [q0,-q1,-q2,-q3]
    temp = quat_mult(q_inv,p_iso)
    p_body=quat_mult(temp,q)
    return np.array(p_body[1:])
def DifQuat(q,w):
    wx,wy,wz = w
    w_q = [0,wx,wy,wz]
    return np.array(0.5 * quat_mult(q,w_q) )
def rotate_by_quat(q, v):
    """Поворот вектора v кватернионом q (q = SSK->ISO)"""
    v_quat = np.array([0, v[0], v[1], v[2]])
    q_conj = np.array([q[0], -q[1], -q[2], -q[3]])
    result = quat_mult(quat_mult(q, v_quat), q_conj)
    return result[1:]
def get_ssk_to_iso(Statement):
    q=Statement[9:13]
    q_sopr = quat_sopr(q)
    s1 = [0,1,0,0]
    s2=[0,0,1,0]
    s3=[0,0,0,1]
    e1 = quat_mult(quat_mult(q,s1),q_sopr)
    e2 = quat_mult(quat_mult(q,s2), q_sopr)
    e3 = quat_mult(quat_mult(q,s3), q_sopr)
    return np.array([e1[1:4],e2[1:4],e3[1:4]])