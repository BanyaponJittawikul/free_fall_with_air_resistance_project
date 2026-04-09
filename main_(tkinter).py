import tkinter as tk
import threading
from physice_logic import *
from time_step_func import *

root = tk.Tk(screenName=None, baseName=None, className='Physics Simulation Tool', useTk=1)
mass_doub = tk.StringVar(value="0.0") #mass
hight_doub = tk.StringVar(value="0.0") #initial high
cross_sec_doub = tk.StringVar(value="0.0") #cross sectional area
drag_co_doub = tk.DoubleVar(value=0.0) #drag coefficient
fluid_den_doub = tk.StringVar(value="1.225") #Fluid Density

objects_value = {"ทรงกลม" : 0.47,
                "ทรงลูกบาศก์" : 1.05}

#time_list = []
#accleration_list = []
#velocity_list = []
#high_list = []
#net_force_list = []

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def validate_float(new_value):
    #ยอมให้เป็นค่าว่าง (เวลาลบทั้งหมด)
    if new_value == "":
        return True
    
    #ยอมให้พิมพ์แค่จุดทศนิยมตัวเดียว (เผื่อกำลังจะพิมพ์ .5 , 0.)
    if new_value == ".":
        return True

    #ตรวจสอบว่าแปลงเป็นตัวเลขทศนิยมได้จริงไหม
    try:
        float(new_value)
        return True
    except ValueError:
        return False

vcmd = root.register(validate_float)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def calculate():
    mass_float = float(mass_doub.get())#มวล(m)
    high_float = float(hight_doub.get())#ความสูง(h)
    cross_sec_float = float(cross_sec_doub.get())#พื้นที่หน้าตัดของวัตถุ(A)
    drag_co_float = float(drag_co_doub.get())#ความเพรียวลม(Cd)
    fluid_den_float = float(fluid_den_doub.get())#ความหนาแน่นของอากาศ(p)
    
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
    

    time_step(physics_dict)




    output = tk.Label(root, text=f"net_force_list {velocity_calculate(high_float)}") #time_step()["net_force_list"]
    output.grid(row = 6, column=1)

    #print(f"time list {time_list}\nacclerationlist {accleration_list}\nvelocity list {velocity_list}\nhigh list {high_list}\nnet force {net_force_list}")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def onclick():
    thread = threading.Thread(target=calculate)

    thread.daemon = True
    thread.start()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def plot_graph():
    pass

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
mass_label = tk.Label(root, text="น้ำหนักวัตถุ(kg)", font=('calibre',10, 'bold'))
mass_entry = tk.Entry(root, textvariable= mass_doub, font=('calibre',10, 'normal'), validate='key', validatecommand=(vcmd, '%P'))

high_label = tk.Label(root, text="ความสูงเริ่มต้นที่ปล่อยวัตถุ(m)", font=('calibre',10, 'bold'))
high_entry = tk.Entry(root, textvariable= hight_doub, font=('calibre',10, 'normal'), validate='key', validatecommand=(vcmd, '%P'))

cross_sec_label = tk.Label(root, text="พื้นที่หน้าตัดของวัตถุที่ปะทะอากาศ(ตารางซม.)", font=('calibre',10, 'bold'))
cross_sec_entry = tk.Entry(root, textvariable= cross_sec_doub, font=('calibre',10, 'normal'), validate='key', validatecommand=(vcmd, '%P'))

drag_co_label = tk.Label(root, text="ค่าสัมประสิทธิ์แรงต้านอากาศ(N)", font=('calibre',10, 'bold'))


fluid_den_label = tk.Label(root, text="ความหนาแน่นของอากาศ(ibs)", font=('calibre',10, 'bold'))
fluid_den_entry = tk.Entry(root, textvariable= fluid_den_doub, font=('calibre',10, 'normal'), validate='key', validatecommand=(vcmd, '%P'))


button = tk.Button(root, text="test", width=50, command=onclick)


mass_label.grid(row=0, column=0, sticky="e")
mass_entry.grid(row=0, column=1)

high_label.grid(row=1, column=0, sticky="e")
high_entry.grid(row=1, column=1)

cross_sec_label.grid(row=2, column=0, sticky="e")
cross_sec_entry.grid(row=2, column=1)

fluid_den_label.grid(row=3, column=0, sticky="e")
fluid_den_entry.grid(row=3, column=1)

drag_co_label.grid(row=4, column=0, sticky="e")
for i, (object_text,object_value) in enumerate(objects_value.items()):
    tk.Radiobutton(root, text=object_text, variable=drag_co_doub, value=object_value).grid(row=4, column=1+i, padx=1)


#output_text = tk.Label(root, text="เวลาที่ใช้ตก", font=('calibre',10, 'bold'))
#output_text.grid(row=6, column=0)


button.grid(row=7, column=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()
