import tkinter as tk
import threading
from physice_logic import *
from time_step_func import *


mass_float = 10.0 #float(input("มวล (kg.) : ")) #มวล(m)
high_float = 10.0 #float(input("ความสูง (m.) : ")) #ความสูง(h)
cross_sec_float = 0.0005 #float(input("พื้นที่หน้าตัดของวัตถุ (m2.) : ")) #พื้นที่หน้าตัดของวัตถุ(A)
drag_co_float = 0.47 #float(input("ความเพรียวลม (N.) : ")) #ความเพรียวลม(Cd)
fluid_den_float = 1.225 #float(input("ความหนาแน่นของอากาศ (ibs.) : ")) #ความหนาแน่นของอากาศ(p)
    
#time = time_calculate(high_float) #หาเวลาทั้งหมดจนกว่าจะตกถึงพื้น(t)
#velocity = velocity_calculate(high_float) #หาความเร็ว(v)
gravitational_force = gravitational_force_calculate(mass_float)#หาแรงโน้มถ่วงตอนดึงวัตถุลง(Fg)
#air_resistance = air_resistance_calculate(fluid_den_float, velocity, drag_co_float, cross_sec_float)#หาแรงต้านอากาศ(Fd)
#net_force = gravitational_force - air_resistance #หาแรงทั้งหมดที่กระทำกับวัตถุ(Fnet)
#acceleration = accleration_calculate(mass_float, air_resistance) #หาความเร่ง ณ ขณะหนึ่ง(a)
    
physics_dict = {"mass" : mass_float,
                "high" : high_float,
                "cross_sec" : cross_sec_float,
                "drag_co" : drag_co_float,
                "fluid_den" : fluid_den_float,
                "gravitational_force" : gravitational_force,
                }
    

data = time_step(physics_dict)

print(data["time_list"])