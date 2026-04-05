from physice_logic import *

dt = 0.00
v = 0.00
h = 0.00

gravitational_force = 9.81
fluid_den_float = 1.225
drag_co_float = 0.47
cross_sec_float = 26
mass_float = 50
high_float = 100

time_list = []
accleration_list = []
velocity_list = []
high_list = []
net_force_list = []


while(high_float > 0):

        
    Fg = gravitational_force
    Fd = air_resistance_calculate(fluid_den_float, v, drag_co_float, cross_sec_float)
    Fnet = Fg - Fd

    a = accleration_calculate(mass_float, Fnet)

    v = v+(a * dt)

    h = h + (v * dt)

    high_float = high_float - h

    
    accleration_list.append(a.__round__(3))
    velocity_list.append(v.__round__(3))
    high_list.append(h.__round__(3))
    net_force_list.append(Fnet.__round__(3))
    time_list.append(dt.__round__(3))
    dt += 0.001

print(f"time list {time_list} จำนวน {len(time_list)}\nacclerationlist {accleration_list} จำนวน {len(accleration_list)}\nvelocity list {velocity_list} จำนวน {len(velocity_list)}\nhigh list {high_list} จำนวน {len(high_list)}\nnet force {net_force_list} จำนวน {len(net_force_list)}")