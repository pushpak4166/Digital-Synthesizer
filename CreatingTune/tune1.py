from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd


#####
root = Tk()
root.title('Audio Synthesizer')
root.minsize(200,800)
root.configure(background='gray')

title = Label(root, text="Tune of Mary Had A Little Lamp", width=500, bg="black", fg="white", padx=20, pady=20, font=("Roboto", 20))
title.pack()
######

class GuitarString:
    def __init__(self, pitch, starting_sample, sampling_freq, stretch_factor):
        """Inits the guitar string."""
        self.pitch = pitch
        self.starting_sample = starting_sample
        self.sampling_freq = sampling_freq
        self.stretch_factor = stretch_factor
        self.init_wavetable()
        self.current_sample = 0
        self.previous_value = 0

    def init_wavetable(self):
        """Generates a new wavetable for the string."""
        wavetable_size = self.sampling_freq // int(self.pitch)
        self.wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)

    def get_sample(self):
        """Returns next sample from string."""
        if self.current_sample >= self.starting_sample:
            current_sample_mod = self.current_sample % self.wavetable.size
            r = np.random.binomial(1, 1 - 1 / self.stretch_factor)
            if r == 0:
                self.wavetable[current_sample_mod] = 0.5 * (self.wavetable[current_sample_mod] + self.previous_value)
            sample = self.wavetable[current_sample_mod]
            self.previous_value = sample
            self.current_sample += 1
        else:
            self.current_sample += 1
            sample = 0
        return sample

fs = 8000

freqs = [180,177,180,177,180,180,180,180,180,180,180,180,180]

unit_delay = fs//1.9

#delays = [(unit_delay+suitable factor)*i for i in range(len(freqs))]
delays = [0,4110,8320,12530,16740,20340,23840,30340,33840,37340,43840,47340,50840]
stretch_factors = [2 * f/180 for f in freqs]

strings = []
for freq, delay, stretch_factor in zip(freqs, delays, stretch_factors):
    string = GuitarString(freq, delay, fs, stretch_factor)
    strings.append(string)
guitar_sound = [sum(string.get_sample() for string in strings) for _ in range(fs *8)]



# Tune of Mary had a little lamp , little lamp , little lamp

def play():
    sd.play(guitar_sound, fs, blocking=True)

w = Button ( root, width="50", text="Play", bg="green", fg="white", padx=30, pady=30, font=("Roboto", 18),command= play ).place(x=310, y=350)


root.mainloop()