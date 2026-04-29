r = initial_state[:3]
r_iso = r / np.linalg.norm(r)
r_norm = np.linalg.norm(r)
r_ssk = to_ssk(initial_state[9:13], r_iso)
Energy =  [m*(Vy**2)/2 + C * (wz**2)/2 - Const*m/x + 3 *Const*(C*(wz**2)-(A+B+C)*(np.linalg.norm(r_ssk))/3)/(2*r_norm)]
Energy1= [m*(Vy**2)/2 - Const*m/x]
r = New_State[:3]


r_iso = r
r_norm = np.linalg.norm(r)
r_ssk = to_ssk(New_State[9:13], r_iso)
New_energy = m * (New_State[3] ** 2 + New_State[4] ** 2 + New_State[5] ** 2) / 2 + 1 / 2 * (
            A * New_State[6] ** 2 + B * New_State[7] ** 2 + C * New_State[8] ** 2) - Const * m / (
                         np.linalg.norm(New_State[:3]) + 3 * Const * (A * (r_ssk[0] ** 2) + B * (r_ssk[1] ** 2)) + C * (
                             r_ssk[2] ** 2) - (A + B + C) * r_norm / 3)
New_energy1 = m * (New_State[3] ** 2 + New_State[4] ** 2 + New_State[5] ** 2) / 2 - Const * m / (
    np.linalg.norm(New_State[:3]))
Energy.append(New_energy)
Energy1.append(New_energy1)