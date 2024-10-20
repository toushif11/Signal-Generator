#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

# Waveform generation functions
def generate_sine_wave(frequency, amplitude, phase, duration, sampling_rate=1000):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    return t, amplitude * np.sin(2 * np.pi * frequency * t + phase)

def generate_square_wave(frequency, amplitude, phase, duration, sampling_rate=1000):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    return t, amplitude * np.sign(np.sin(2 * np.pi * frequency * t + phase))

def generate_triangular_wave(frequency, amplitude, phase, duration, sampling_rate=1000):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    return t, amplitude * 2 * np.abs(2 * (t * frequency - np.floor(t * frequency + 0.5))) - amplitude

# Function to plot the waveforms
def plot_waveform(t, signal, title):
    plt.figure(figsize=(10, 4))
    plt.plot(t, signal)
    plt.title(title)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

# User inputs for waveform parameters
def main():
    # Input parameters
    waveform_type = input("Enter the waveform type (sine/square/triangular): ").strip().lower()
    frequency = float(input("Enter the frequency (Hz): "))
    amplitude = float(input("Enter the amplitude: "))
    phase = float(input("Enter the phase (radians): "))
    duration = float(input("Enter the duration (seconds): "))

    # Generate and plot the chosen waveform
    if waveform_type == 'sine':
        t, signal = generate_sine_wave(frequency, amplitude, phase, duration)
        plot_waveform(t, signal, f"Sine Wave: {frequency} Hz, Amplitude: {amplitude}, Phase: {phase}")
    elif waveform_type == 'square':
        t, signal = generate_square_wave(frequency, amplitude, phase, duration)
        plot_waveform(t, signal, f"Square Wave: {frequency} Hz, Amplitude: {amplitude}, Phase: {phase}")
    elif waveform_type == 'triangular':
        t, signal = generate_triangular_wave(frequency, amplitude, phase, duration)
        plot_waveform(t, signal, f"Triangular Wave: {frequency} Hz, Amplitude: {amplitude}, Phase: {phase}")
    else:
        print("Invalid waveform type. Please choose sine, square, or triangular.")

if __name__ == "__main__":
    main()


# In[ ]:




