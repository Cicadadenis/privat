from tkinter import *
from ttkbootstrap.widgets import Meter
root = Tk()
root.title('Example of Tkinter module')
root.geometry('{}x{}'.format(800,600))

frame_top    = Frame(root, width=800, height=120, bg="#154e72")
frame_left   = Frame(root, width=240, height=420, bg="#154e72")
frame_right  = Frame(root, width=550, height=420, bg="#154e72")
frame_bottom = Frame(root, width=800, height=80,  bg="#154e72")

horizontal_frame_1 = Frame(root, width=800, height=5)
horizontal_frame_1.grid(row=1, columnspan=2, sticky='ew')

root.grid_rowconfigure(1,weight=1)
root.grid_columnconfigure(0,weight=1)

frame_top.grid  (row=0, columnspan=3, sticky="ew")

vertical_frame = Frame(root, width=10, height=420)
vertical_frame.grid(row=2, column=1)
frame_left.grid (row=2, column=0, sticky="w")
frame_right.grid(row=2, column=2, sticky="e")



horizontal_frame_2 = Frame(root, width=800, height=5)
horizontal_frame_2.grid(row=3, columnspan=3)

frame_bottom.grid(row=4, columnspan=3, sticky="ew")
m = Meter(
    frame_top,
    showtext="6666",
    metersize=100,
    amountused=20,
    padding=30,
    metertype='semi',
    subtext='Акаунтов', 
    subtextfont="-size 10",
    interactive=True
)
m.pack(padx=49, pady=0, ipady=30)
label_1 = Label(frame_top,  text="Cicada3301 Telegram-Satana",bg="#154e72")

label_1.pack(padx=49, pady=0, ipady=30)
frame_top.grid_propagate()

root.mainloop()