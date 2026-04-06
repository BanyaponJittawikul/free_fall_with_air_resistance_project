from physice_logic import *

def time_step(physics_dict):
    time_list = []
    accleration_list = []
    velocity_list = []
    high_list = []
    net_force_list = []

    dt = 0.00
    v = 0.00
    h = 0.00
    while(physics_dict['high'] > 0):

            
        Fg = physics_dict['gravitational_force']
        Fd = air_resistance_calculate(physics_dict['fluid_den'], v, physics_dict['drag_co'], physics_dict['cross_sec'])
        Fnet = Fg - Fd

        a = accleration_calculate(physics_dict['mass'], Fnet)

        v = v+(a * dt)

        h = h + (v * dt)

        physics_dict['high'] = physics_dict['high'] - h

        
        accleration_list.append(a.__round__(3))
        velocity_list.append(v.__round__(3))
        high_list.append(h.__round__(3))
        net_force_list.append(Fnet.__round__(3))
        time_list.append(dt.__round__(3))
        dt += 0.001

    
    #print(f"time list {time_list} จำนวน {len(time_list)}\nacclerationlist {accleration_list} จำนวน {len(accleration_list)}\nvelocity list {velocity_list} จำนวน {len(velocity_list)}\nhigh list {high_list} จำนวน {len(high_list)}\nnet force {net_force_list} จำนวน {len(net_force_list)}")
    return {"time_list" : time_list,
            "accleration_list" : accleration_list,
            "velocity_list" : velocity_list,
            "high_list" : high_list,
            "net_force_list" : net_force_list}

