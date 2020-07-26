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
root.minsize(500,900)
root.configure(background='gray')

title = Label(root, text="Plucked String Sound Synthesis With Longer Decay", width=500, bg="black", fg="white", padx=20, pady=20, font=("Roboto", 20))
title.pack()

frequency = Label(root, text="Stretch Factors (s):", bg="gray", fg="white", padx=20, pady=20, font=("Roboto", 12)).place(x=80, y=100)
frequency1 = Label(root, text="Fundamental Frequency (fo):", bg="gray", fg="white", padx=20, pady=20, font=("Roboto", 12)).place(x=80, y=150)
   #frequency_input_area = Entry(root, width=40).place(x=40, y=150)

# 1st entry
frame0 = Frame(root, borderwidth=2, relief=SUNKEN)
e0 = Entry(frame0, borderwidth=2, relief=FLAT)
e0.pack()
frame0.place(x=250, y=120)
# 2nd entry
frame1 = Frame(root, borderwidth=2, relief=SUNKEN)
e1 = Entry(frame1, borderwidth=2, relief=FLAT)
e1.pack()
frame1.place(x=370, y=120)
# 3rd entry
frame2 = Frame(root, borderwidth=2, relief=SUNKEN)
e2 = Entry(frame2, borderwidth=2, relief=FLAT)
e2.pack()
frame2.place(x=490, y=120)
# 4th entry
frame3 = Frame(root, borderwidth=2, relief=SUNKEN)
e3 = Entry(frame3, borderwidth=2, relief=FLAT)
e3.pack()
frame3.place(x=610, y=120)
# 5th entry
frame4 = Frame(root, borderwidth=2, relief=SUNKEN)
e4 = Entry(frame4, borderwidth=2, relief=FLAT)
e4.pack()
frame4.place(x=730, y=120)

# fundamental frequency
frame5 = Frame(root, borderwidth=2, relief=SUNKEN)
e5 = Entry(frame5, borderwidth=2, relief=FLAT)
e5.pack()
frame5.place(x=330, y=170)

s = np.zeros(5)
def check():
    s[0] = float(e0.get())
    print(s[0])
    print(type(s[0]))
    s[1] = float(e1.get())
    print(s[1])
    print(type(s[1]))
    s[2] = float(e2.get())
    print(s[2])
    print(type(s[2]))
    s[3] = float(e3.get())
    print(s[3])
    print(type(s[3]))
    s[4] = float(e4.get())
    print(s[4])
    print(type(s[4]))
    f0 = float(e5.get())
    print(f0)

    #wavetable_size = fs // f0
    #wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)

    frequency2 = Label(root, text="(Wait for 4 sec before pressing another button for better analysis)", bg="gray",
                       fg="white", padx=20, pady=20, font=("Roboto", 12)).place(x=80, y=350)
    def karplus_strong_decay(wavetable, n_samples, stretch_factor):
        """Using a stretch factor to controlling the decay."""
        samples = []
        current_sample = 0
        previous_value = 0
        while len(samples) < n_samples:
            r = np.random.binomial(1, 1 - 1 / stretch_factor)
            if r == 0:
                wavetable[current_sample] = 0.5 * (wavetable[current_sample] + previous_value)
            samples.append(wavetable[current_sample])
            previous_value = samples[-1]
            current_sample += 1
            current_sample = current_sample % wavetable.size
        return np.array(samples)

    i = -1

    rows, cols = (6,4*fs)
    waveforms = [[0 for i in range(cols)] for j in range(rows)]

    for ind, stretch_factor in enumerate(s):
        i = i + 1
        wavetable_size = fs // int(f0)
        wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)
        arr = karplus_strong_decay(wavetable, 4*fs, stretch_factor)
        for k in range(4*fs):
            waveforms[i][k] = arr[k]


        def play(i):
            print(i)
            sd.play(waveforms[i], fs, blocking=True)

        if i==0:
            w = Button(root, width="5", text="s="+str(s[0]), bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(0)).place(x=100, y=400)
        elif i==1:
            w = Button(root, width="5", text="s="+str(s[1]), bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(1)).place(x=160, y=400)
        elif i==2:
            w = Button(root, width="5", text="s="+str(s[2]), bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(2)).place(x=220, y=400)
        elif i==3:
            w = Button(root, width="5", text="s="+str(s[3]), bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(3)).place(x=280, y=400)
        else :
            w = Button(root, width="5", text="s="+str(s[4]), bg="green", fg="white", padx=5, pady=5, font=("Roboto", 12),
               command=lambda:play(4)).place(x=340, y=400)





w = Button ( root, width="20", text="Enter", bg="green", fg="white", padx=10, pady=10, font=("Roboto", 12),command= check ).place(x=100, y=250)
#w1 = Button ( root, width="20", text="Enter", bg="green", fg="white", padx=10, pady=10, font=("Roboto", 12),command= check ).place(x=500, y=200)

#array = Label(root, text="Array :", bg="gray", fg="white", padx=20, pady=20, font=("Roboto", 12)).place(x=50, y=200)
# frequency_input_area = Entry(root, width=40).place(x=40, y=150)
#frame2 = Frame(root, borderwidth=2, relief=SUNKEN, width=300)
#entry2 = Entry(frame2, borderwidth=8, relief=FLAT)
#entry2.pack()
#frame2.place(x=220, y=210)


root.mainloop()
