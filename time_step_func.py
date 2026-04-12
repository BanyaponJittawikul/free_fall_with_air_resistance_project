from physice_logic import *

def time_step(physics_dict):
    time_list = []
    accleration_list = []
    velocity_list = []
    high_list = []
    net_force_list = []

    #เก็บค่าที่ดึงมาแล้วไว้ในตัวแปร

    m = physics_dict["mass"] #float(input("มวล (kg.) : ")) #มวล(m)
    high = physics_dict["high"] #float(input("ความสูง (m.) : ")) #ความสูง(h)
    A = physics_dict["cross_sec"] #float(input("พื้นที่หน้าตัดของวัตถุ (m2.) : ")) #พื้นที่หน้าตัดของวัตถุ(A)
    Cd = physics_dict["drag_co"] #float(input("ความเพรียวลม (N.) : ")) #ความเพรียวลม(Cd)
    p = physics_dict["fluid_den"] #float(input("ความหนาแน่นของอากาศ (kg/m^3.) : ")) #ความหนาแน่นของอากาศ(p)
    Fg = physics_dict["gravitational_force"]

    dt = 0.001
    v = 0.00
    h = 0.00
    t = 0.00

    #ลูปคำนวน time step ของ freefall
    while(high > 0):
        #Fg = gravitational_force
        Fd = 0.5*p*(v**2)*Cd*A
        Fnet = Fg - Fd
        a = ((m*9.81)-Fd)/m #accleration_calculate(mass_float, Fnet)

        v = v + (a * dt)

        h = h + (v * dt)

        high = high - h

        #คำนวนค่าที่ต้องการแล้วเก็บไว้ใน list

        accleration_list.append(a.__round__(3))
        velocity_list.append(v.__round__(3))
        high_list.append(h.__round__(3))
        net_force_list.append(Fnet.__round__(3))
        time_list.append(t.__round__(3))

        #เพิ่มเวลาของ t ทีละ 0.001
        t += dt
    
    #print(f"time list {time_list} จำนวน {len(time_list)}\nacclerationlist {accleration_list} จำนวน {len(accleration_list)}\nvelocity list {velocity_list} จำนวน {len(velocity_list)}\nhigh list {high_list} จำนวน {len(high_list)}\nnet force {net_force_list} จำนวน {len(net_force_list)}")
    return {"time_list" : time_list,
            "accleration_list" : accleration_list,
            "velocity_list" : velocity_list,
            "high_list" : high_list,
            "net_force_list" : net_force_list}

