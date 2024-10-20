import numpy as np
import matplotlib.pyplot as plt

def generate_square_wave(amplitude, phase, frequency, duration):
    t = np.linspace(0, duration, 1000)  # time vector
    wave = amplitude * np.sign(np.sin(frequency * t + phase))  # square wave generation
    return t, wave

def main():
    # Taking inputs from the user
    amplitude = float(input("Enter the amplitude of the square wave: "))
    phase = float(input("Enter the phase (in radians) of the square wave: "))
    frequency = float(input("Enter the frequency (in radians/s) of the square wave: "))
    duration = float(input("Enter the duration (in seconds) for which to generate the wave: "))
    
    # Generate the square wave
    t, wave = generate_square_wave(amplitude, phase, frequency, duration)
    
    # Plotting the square wave
    plt.figure(figsize=(10, 4))
    plt.plot(t, wave, label='Square Wave', color='blue')
    plt.title('Square Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.xlim(0, duration)
    plt.ylim(-amplitude * 1.5, amplitude * 1.5)
    plt.show()

if __name__ == "__main__":
    main()




