import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio
import wave
import sounddevice as sd
from tkinter import *
from PIL import Image
from PIL import ImageTk


fs = 8000

root = Tk()
root.title('Audio Synthesizer')
root.minsize(800,800)
root.configure(background='gray')

title = Label(root, text="Plucked String Sound Synthesis", width=500, bg="black", fg="white", padx=20, pady=20, font=("Roboto", 20))
title.pack()

frequency = Label(root, text="Frequency f0  (in Hz) :", bg="gray", fg="white", padx=20, pady=20, font=("Roboto", 12)).place(x=50, y=100)
   #frequency_input_area = Entry(root, width=40).place(x=40, y=150)
frame = Frame(root, borderwidth=2, relief=SUNKEN)
e = Entry(frame, borderwidth=8, relief=FLAT)
e.pack()
frame.place(x=240, y=110)


def check():
    f = e.get()
    f0 = float(f)
    print(f)
    print(type(f))
    print(f0)
    print(type(f0))

    #wavetable_size = fs // f0
    #wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)

    def karplus_strong(wavetable, n_samples):
        """Synthesizes a new waveform from an existing wavetable, modifies last sample by averaging."""
        samples = []
        current_sample = 0
        previous_value = 0
        while len(samples) < n_samples:
            wavetable[current_sample] = 0.5 * (wavetable[current_sample] + previous_value)
            samples.append(wavetable[current_sample])
            previous_value = samples[-1]
            current_sample += 1
            current_sample = current_sample % wavetable.size
        return np.array(samples)

    freqs = np.logspace(0, 1, num=13, base=2) * f0
    i = -1

    rows, cols = (13,fs)
    sam = [[0 for i in range(cols)] for j in range(rows)]

    for freq in freqs:
        i = i + 1
        wavetable_size = fs // int(freq)
        wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)
        arr = karplus_strong(wavetable, 1 * fs)

        for k in range(fs):
            sam[i][k]=arr[k]



        def play(i):
            print(i)
            sd.play(sam[i], fs, blocking=True)

        if i==0:
            w = Button(root, width="5", text="F0", bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(0)).place(x=50, y=300)
        elif i==1:
            w = Button(root, width="5", text="F1", bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(1)).place(x=120, y=300)
        elif i==2:
            w = Button(root, width="5", text="F2", bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(2)).place(x=190, y=300)
        elif i==3:
            w = Button(root, width="5", text="F3", bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(3)).place(x=260, y=300)
        elif i==4:
            w = Button(root, width="5", text="F4", bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(4)).place(x=330, y=300)
        elif i==5:
            w = Button(root, width="5", text="F5", bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(5)).place(x=400, y=300)
        elif i==6:
            w = Button(root, width="5", text="F6", bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(6)).place(x=470, y=300)
        elif i==7:
            w = Button(root, width="5", text="F7", bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(7)).place(x=540, y=300)
        elif i==8:
            w = Button(root, width="5", text="F8", bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(8)).place(x=610, y=300)
        elif i==9:
            w = Button(root, width="5", text="F9", bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(9)).place(x=680, y=300)
        elif i==10:
            w = Button(root, width="5", text="F10", bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(10)).place(x=750, y=300)
        elif i==11:
            w = Button(root, width="5", text="F11", bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(11)).place(x=820, y=300)
        else :
            w = Button(root, width="5", text="F12", bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(12)).place(x=890, y=300)




w = Button ( root, width="20", text="Enter", bg="green", fg="white", padx=10, pady=10, font=("Roboto", 12),command= check ).place(x=500, y=105)

#array = Label(root, text="Array :", bg="gray", fg="white", padx=20, pady=20, font=("Roboto", 12)).place(x=50, y=200)
# frequency_input_area = Entry(root, width=40).place(x=40, y=150)
#frame2 = Frame(root, borderwidth=2, relief=SUNKEN, width=300)
#entry2 = Entry(frame2, borderwidth=8, relief=FLAT)
#entry2.pack()
#frame2.place(x=220, y=210)


root.mainloop()
