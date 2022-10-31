#####################################################
#                                                   #
#                                                   #
#                 old version                       #
#                using tkinter                      #
#                 see the new                       #
#               in main.py file                     #
#                                                   #
#                                                   #
######################################################

import tkinter as tk
import math as m

details = {}
data = {}

def addLine():
    try:
        line_name = line_input.get()
        length = float(length_input.get())
        azimuth_degree = int(degree_input.get())
        azimuth_minutes = int(minutes_input.get())
        azimuth_seconds = float(seconds_input.get())
    except:
        length_result["text"]="wrong input"
    azimuth_degree *= (m.pi / 180)
    azimuth_minutes *= (m.pi / 180)
    azimuth_seconds *= (m.pi / 180)
    details[line_name] = {"length":length, "degree":azimuth_degree, "minutes":azimuth_minutes, "seconds":azimuth_seconds}
    vertical_compound = length * (m.cos((((azimuth_seconds / 60) + azimuth_minutes) / 60) + azimuth_degree))
    horizontal_compound = length * (m.sin((((azimuth_seconds / 60) + azimuth_minutes) / 60) + azimuth_degree))
    data[line_name] = [vertical_compound, horizontal_compound]
    line_input.delete(0, "end")
    length_input.delete(0, "end")
    degree_input.delete(0, "end")
    minutes_input.delete(0, "end")
    seconds_input.delete(0, "end")

def seeResult():
    vc_sum = [i[0] for i in data.values()]
    hc_sum = [i[1] for i in data.values()]
    unknownAngle = str(m.atan(sum(hc_sum)/sum(vc_sum)) * 180 / m.pi)
    degree = unknownAngle[:unknownAngle.index('.')]
    minutes = str(float("0." + unknownAngle[unknownAngle.index('.')+1:]) * 60)
    seconds = str(float("0." + minutes[minutes.index('.')+1:]) * 60)
    minutes = minutes[:minutes.index('.')]
    degree_result['text'] = f"degree is {degree}"
    minutes_result['text'] = f"minutes are {minutes}"
    seconds_result['text'] = f"seconds are {round(float(seconds), 2)}"
    finalLength = abs(sum(vc_sum) / m.cos(float(unknownAngle) * (m.pi / 180)))
    length_result['text'] = f"length is {round(finalLength, 3)}"
    


window = tk.Tk()
window.title("الأرصاد الناقصة (طول الضلع و انحرافه)")

coloredbg = tk.Frame(master=window, bg='#acdedd')
coloredbg.pack(fill=tk.BOTH, expand=True)

frm_entry = tk.Frame(master=coloredbg, bg="#acdedd")

line_name= tk.Label(master=frm_entry, text="line", bg="#acdedd", font=("Poppins", 16))
line_input = tk.Entry(master=frm_entry, width=10, bg="#56abcb", font=("Poppins", 16))

length = tk.Label(master=frm_entry, text="length", bg="#acdedd", font=("Poppins", 16))
length_input = tk.Entry(master=frm_entry, width=10, bg="#56abcb", font=("Poppins", 16))

degree = tk.Label(master=frm_entry, text="degree", bg="#acdedd", font=("Poppins", 16))
degree_input = tk.Entry(master=frm_entry, width=10, bg="#56abcb", font=("Poppins", 16))

minutes = tk.Label(master=frm_entry, text="minutes", bg="#acdedd", font=("Poppins", 16))
minutes_input = tk.Entry(master=frm_entry, width=10, bg="#56abcb", font=("Poppins", 16))

seconds = tk.Label(master=frm_entry, text="seconds", bg="#acdedd", font=("Poppins", 16))
seconds_input = tk.Entry(master=frm_entry, width=10, bg="#56abcb", font=("Poppins", 16))

# Create the conversion Button and result display Label


length_result = tk.Label(master=frm_entry, text="", bg="#acdedd", fg="#2267a9", font=("Poppins", 20, "bold"))
degree_result = tk.Label(master=frm_entry, text="", bg="#acdedd", fg="#2267a9", font=("Poppins", 20, "bold"))
minutes_result = tk.Label(master=frm_entry, text="", bg="#acdedd", fg="#2267a9", font=("Poppins", 20, "bold"))
seconds_result = tk.Label(master=frm_entry, text="", bg="#acdedd", fg="#2267a9", font=("Poppins", 20, "bold"))

# Set-up the layout using the .grid() geometry manager

line_name.grid(row=0, column=0, columnspan=2, sticky="ewns", pady=20, padx=20)
line_input.grid(row=0, column=2, columnspan=2, sticky="ewns", pady=20, padx=20)

length.grid(row=1, column=0, columnspan=2, sticky="ewns", pady=20, padx=20)
length_input.grid(row=1, column=2, columnspan=2, sticky="ewns", pady=20, padx=20)

degree.grid(row=2, column=0, columnspan=2, sticky="ewns", pady=20, padx=20)
degree_input.grid(row=2, column=2, columnspan=2, sticky="ewns", pady=20, padx=20)

minutes.grid(row=3, column=0, columnspan=2, sticky="ewns", pady=20, padx=20)
minutes_input.grid(row=3, column=2, columnspan=2, sticky="ewns", pady=20, padx=20)

seconds.grid(row=4, column=0, columnspan=2, sticky="ewns", pady=20, padx=20)
seconds_input.grid(row=4, column=2, columnspan=2, sticky="ewns", pady=20, padx=20)

btn_add_line = tk.Button(
    master=frm_entry,
    text="Add new line",
    command=addLine
)
btn_convert = tk.Button(
    master=frm_entry,
    text="See the result",
    command=seeResult
)
btn_convert.grid(row=5, column=2, columnspan=2, sticky="ewns", pady=20, padx=20)
btn_add_line.grid(row=5, column=0, columnspan=2, sticky="ewns", pady=20, padx=20)

length_result.grid(row=6, columnspan=2, sticky="ewns", pady=20, padx=20)
degree_result.grid(row=6, column=3, columnspan=2, sticky="ewns", pady=20, padx=20)
minutes_result.grid(row=7, columnspan=2, sticky="ewns", pady=20, padx=20)
seconds_result.grid(row=7, column=3, columnspan=2, sticky="ewns", pady=20, padx=20)

frm_entry.pack(anchor="center")

# Run the application
window.mainloop()