import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio
import wave
import sounddevice as sd
from tkinter import *
from PIL import Image
from PIL import ImageTk


fs = 8000
wavetable_size = fs // 40
wavetable = np.ones(wavetable_size)



root = Tk()
root.title('Audio Synthesizer')
root.minsize(300,300)
root.configure(background='gray')

title = Label(root, text="Drum Sound Synthesizer", width=500, bg="black", fg="white", padx=20, pady=20, font=("Roboto", 20))
title.pack()

frequency = Label(root, text="Blend factor (b):", bg="gray", fg="white", padx=20, pady=20, font=("Roboto", 12)).place(x=50, y=100)
   #frequency_input_area = Entry(root, width=40).place(x=40, y=150)
frame = Frame(root, borderwidth=2, relief=SUNKEN)
e = Entry(frame, borderwidth=8, relief=FLAT)
e.pack()
frame.place(x=220, y=110)


def check():
    b = e.get()
    b1 = float(b)
    print(b)
    print(type(b))
    print(b1)
    print(type(b1))

    def karplus_strong_drum(wavetable, n_samples, prob):
        """Synthesizes a new waveform from an existing wavetable, modifies last sample by averaging."""
        samples = []
        current_sample = 0
        previous_value = 0
        while len(samples) < n_samples:
            r = np.random.binomial(1, prob)
            sign = float(r == 1) * 2 - 1
            wavetable[current_sample] = sign * 0.5 * (wavetable[current_sample] + previous_value)
            samples.append(wavetable[current_sample])
            previous_value = samples[-1]
            current_sample += 1
            current_sample = current_sample % wavetable.size
        return np.array(samples)

    sample1 = karplus_strong_drum(wavetable, 1 * fs,b1)

    def play():
        sd.play(sample1, fs, blocking=True)

    w = Button(root, width="30", text="Play", bg="green", fg="white", padx=10, pady=10, font=("Roboto", 12),
               command=play).place(x=60, y=300)






w = Button ( root, width="30", text="Enter", bg="green", fg="white", padx=10, pady=10, font=("Roboto", 12),command= check ).place(x=60, y=200)

#array = Label(root, text="Array :", bg="gray", fg="white", padx=20, pady=20, font=("Roboto", 12)).place(x=50, y=200)
# frequency_input_area = Entry(root, width=40).place(x=40, y=150)
#frame2 = Frame(root, borderwidth=2, relief=SUNKEN, width=300)
#entry2 = Entry(frame2, borderwidth=8, relief=FLAT)
#entry2.pack()
#frame2.place(x=220, y=210)




root.mainloop()

