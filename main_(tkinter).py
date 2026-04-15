import tkinter as tk
import threading
from physice_logic import *
from time_step_func import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np

root = tk.Tk(screenName=None, baseName=None, className='Physics Simulation Tool', useTk=1)
mass_doub = tk.StringVar(value="0.0") #mass
hight_doub = tk.StringVar(value="0.0") #initial high
cross_sec_doub = tk.StringVar(value="0.0") #cross sectional area
drag_co_doub = tk.StringVar(value='0.47') #drag coefficient
fluid_den_doub = tk.StringVar(value="1.225") #Fluid Density
x_axis_value = tk.StringVar(value="time_list") #x axis
y_axis_value = tk.StringVar(value="time_list") #y axis


objects_value = {"ทรงกลม" : 0.47,
                "ทรงลูกบาศก์" : 1.05}


plot_graph_value = {"time list" : "time_list",
            "accleration list" : "accleration_list",
            "velocity list" : "velocity_list",
            "high list" : "high_list",
            "net force list" : "net_force_list"}



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
    

    all_data = time_step(physics_dict)


    output = tk.Label(root, text=f"คำนวนเรียบร้อย") #time_step()["net_force_list"]
    output.grid(row=5, column=2)
    

    #print(f"time list {time_list}\nacclerationlist {accleration_list}\nvelocity list {velocity_list}\nhigh list {high_list}\nnet force {net_force_list}")

    return {"time_list" : all_data["time_list"],
            "accleration_list" : all_data["accleration_list"],
            "velocity_list" : all_data["velocity_list"],
            "high_list" : all_data["high_list"],
            "net_force_list" : all_data["net_force_list"]}


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def onclick():
    thread = threading.Thread(target=calculate)

    thread.daemon = True
    thread.start()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#list for plot graph




def plot_graph():
    all_list_data = calculate()
    x_axis = x_axis_value.get()
    y_axis = y_axis_value.get()

    match x_axis:
        case "time_list":
            x_axis_text = "time"
            x_axis_plot = all_list_data["time_list"]
        case "accleration_list":
            x_axis_text = "accleration"
            x_axis_plot = all_list_data["accleration_list"]
        case "velocity_list":
            x_axis_text = "velocity"
            x_axis_plot = all_list_data["velocity_list"]
        case "high_list":
            x_axis_text = "high"
            x_axis_plot = all_list_data["high_list"]
        case "net_force_list":
            x_axis_text = "net force"
            x_axis_plot = all_list_data["net_force_list"]


    match y_axis:
        case "time_list":
            y_axis_text = "time"
            y_axis_plot = all_list_data["time_list"]
        case "accleration_list":
            y_axis_text = "accleration"
            y_axis_plot = all_list_data["accleration_list"]
        case "velocity_list":
            y_axis_text = "velocity"
            y_axis_plot = all_list_data["velocity_list"]
        case "high_list":
            y_axis_text = "high"
            y_axis_plot = all_list_data["high_list"]
        case "net_force_list":
            y_axis_text = "net force"
            y_axis_plot = all_list_data["net_force_list"]




    fig = Figure(figsize=(5, 4), dpi=100)
    plt = fig.add_subplot(111)

    xplot = np.array(x_axis_plot)
    yplot = np.array(y_axis_plot)

    plt.plot(xplot, yplot)
    plt.set_xlabel(x_axis_text)
    plt.set_ylabel(y_axis_text)


    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    canvas.get_tk_widget().grid(row = 6, column=1)

    

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


plot_lable_x = tk.Label(root, text="กราฟแกน x", font=('calibre',10, 'bold'))


plot_lable_y = tk.Label(root, text="กราฟแกน y", font=('calibre',10, 'bold'))


button = tk.Button(root, text="calculate list", width=50, command=onclick)

plot_graph_button = tk.Button(root, text="plot", width=50, command=plot_graph)


mass_label.grid(row=0, column=0, sticky="e")
mass_entry.grid(row=0, column=1)

high_label.grid(row=1, column=0, sticky="e")
high_entry.grid(row=1, column=1)

cross_sec_label.grid(row=2, column=0, sticky="e")
cross_sec_entry.grid(row=2, column=1)

fluid_den_label.grid(row=3, column=0, sticky="e")
fluid_den_entry.grid(row=3, column=1)

drag_co_label.grid(row=4, column=0, sticky="e")
drag_co_label_containner = tk.Frame(root)
drag_co_label_containner.grid(row=4, column=1, padx=1)

for i, (object_text,object_value) in enumerate(objects_value.items()):
    drag_co_rb = tk.Radiobutton(drag_co_label_containner, text=object_text, variable=drag_co_doub, value=object_value)
    drag_co_rb.pack(anchor="w")


plot_lable_x.grid(row = 0, column=3, sticky="e")
x_axis_containner = tk.Frame(root)
x_axis_containner.grid(row = 1, column = 3)


for x, (x_graph_text, x_graph_value) in enumerate(plot_graph_value.items()):
    x_axis_rb = tk.Radiobutton(x_axis_containner, text=x_graph_text, variable=x_axis_value, value=x_graph_value)
    x_axis_rb.pack(anchor="w")


plot_lable_y.grid(row = 0, column=4, sticky="e")
y_axis_containner = tk.Frame(root)
y_axis_containner.grid(row = 1, column = 4)

for y, (y_graph_text, y_graph_value) in enumerate(plot_graph_value.items()):
    y_axis_rb = tk.Radiobutton(y_axis_containner, text=y_graph_text, variable=y_axis_value, value=y_graph_value)
    y_axis_rb.pack(anchor="w")


#output_text = tk.Label(root, text="เวลาที่ใช้ตก", font=('calibre',10, 'bold'))
#output_text.grid(row=6, column=0)


button.grid(row=5, column=0)
plot_graph_button.grid(row=5, column=1)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()
