import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import welch

def load_signal(file_path, num_channels=2, Fs=360):
    Ts = 1 / Fs
    signal = np.fromfile(file_path, dtype=np.int16).reshape(-1, num_channels)
    t = np.arange(len(signal)) / Fs
    return signal, t, Fs, Ts

def compute_statistics(signal):
    stats = {
        "mean": np.mean(signal, axis=0),
        "median": np.median(signal, axis=0),
        "std": np.std(signal, axis=0),
        "min": np.min(signal, axis=0),
        "max": np.max(signal, axis=0),
    }
    print("Estadísticos antes de la Transformada de Fourier:")
    for key, value in stats.items():
        print(f"{key}: {value}")
    return stats

def compute_fourier(signal, Ts):
    N = len(signal)
    frequencies = fftfreq(N, Ts)
    spectrum = np.abs(fft(signal, axis=0))
    return frequencies, spectrum

def compute_psd(signal, Fs):
    freqs, psd_ch1 = welch(signal[:, 0], Fs, nperseg=1024)
    freqs, psd_ch2 = welch(signal[:, 1], Fs, nperseg=1024)
    return freqs, psd_ch1, psd_ch2

def compute_frequency_statistics(frequencies, spectrum):
    mean_freq = np.sum(frequencies[:, None] * spectrum, axis=0) / np.sum(spectrum, axis=0)
    median_freq = frequencies[np.argmax(np.cumsum(spectrum, axis=0) >= np.sum(spectrum, axis=0) / 2, axis=0)]
    std_freq = np.sqrt(np.sum((frequencies[:, None] - mean_freq) ** 2 * spectrum, axis=0) / np.sum(spectrum, axis=0))
    print("Estadísticos después de la Transformada de Fourier:")
    print(f"Frecuencia media: {mean_freq}")
    print(f"Frecuencia mediana: {median_freq}")
    print(f"Desviación estándar: {std_freq}")
    return mean_freq, median_freq, std_freq

def compute_convolution(x, h):
    return np.convolve(x, h)

def compute_correlation(x1, x2):
    return np.correlate(x1, x2, mode='full')

def plot_signals(t, signal):
    plt.figure(figsize=(12, 4))
    plt.plot(t, signal[:, 0], label="Canal 1")
    plt.plot(t, signal[:, 1], label="Canal 2", alpha=0.7)
    plt.title("Señal en el tiempo")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend()
    plt.grid()
    plt.show()

def plot_fourier(frequencies, spectrum, N):
    plt.figure(figsize=(10, 4))
    plt.plot(frequencies[:N // 2], spectrum[:N // 2, 0], label="Canal 1")
    plt.plot(frequencies[:N // 2], spectrum[:N // 2, 1], label="Canal 2", alpha=0.7)
    plt.title("Transformada de Fourier")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.legend()
    plt.grid()
    plt.show()

def plot_psd(freqs, psd_ch1, psd_ch2):
    plt.figure(figsize=(10, 4))
    plt.semilogy(freqs, psd_ch1, label="Canal 1")
    plt.semilogy(freqs, psd_ch2, label="Canal 2", alpha=0.7)
    plt.title("Densidad Espectral de Potencia")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("PSD")
    plt.legend()
    plt.grid()
    plt.show()

def plot_histogram(signal):
    plt.figure(figsize=(6, 4))
    plt.hist(signal[:, 0], bins=30, alpha=0.7, label="Canal 1")
    plt.hist(signal[:, 1], bins=30, alpha=0.7, label="Canal 2")
    plt.title("Histograma de la señal")
    plt.xlabel("Amplitud")
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.grid()
    plt.show()

def plot_convolution(x, h, y):
    plt.figure(figsize=(10, 4))
    plt.subplot(3, 1, 1)
    plt.stem(x)
    plt.title("Señal x[n]")
    plt.grid()
    plt.subplot(3, 1, 2)
    plt.stem(h)
    plt.title("Señal h[n]")
    plt.grid()
    plt.subplot(3, 1, 3)
    plt.stem(y)
    plt.title("Convolución x*h")
    plt.grid()
    plt.tight_layout()
    plt.show()

def plot_correlation(x1, x2, corr):
    plt.figure(figsize=(10, 4))
    plt.stem(range(-len(x1) + 1, len(x1)), corr)
    plt.title("Correlación cruzada entre señales")
    plt.grid()
    plt.show()

# Main execution
file_path = r"C:\Users\juany\OneDrive\Escritorio\LabSeñales\Lab2\01.dat"
signal, t, Fs, Ts = load_signal(file_path)
statistics = compute_statistics(signal)
frequencies, spectrum = compute_fourier(signal, Ts)
freqs, psd_ch1, psd_ch2 = compute_psd(signal, Fs)
mean_freq, median_freq, std_freq = compute_frequency_statistics(frequencies, spectrum)

# Convolución y correlación de señales de prueba
x1 = np.array([1, 0, 0, 0, 9, 7, 1, 3, 6, 4])
h1 = np.array([5, 6, 0, 0, 6, 1, 6])
y1 = compute_convolution(x1, h1)
plot_convolution(x1, h1, y1)

x2 = np.cos(2 * np.pi * 100 * np.arange(9) * Ts)
x3 = np.sin(2 * np.pi * 100 * np.arange(9) * Ts)
corr = compute_correlation(x2, x3)
plot_correlation(x2, x3, corr)

plot_signals(t, signal)
plot_fourier(frequencies, spectrum, len(signal))
plot_psd(freqs, psd_ch1, psd_ch2)
plot_histogram(signal)

(statistics, mean_freq, median_freq, std_freq)

