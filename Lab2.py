import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import welch

#1 Definir señales
x1 = np.array([1, 0, 0, 0, 9, 7, 1, 3, 6, 4])
h1 = np.array([5, 6, 0, 0, 6, 1, 6])
y1 = np.convolve(x1, h1)

x2 = np.array([1, 0, 2, 5, 4, 6, 1, 2, 4, 5])
h2 = np.array([5, 6, 0, 0, 6, 1, 1])
y2 = np.convolve(x2, h2)

# Graficar señales
plt.figure(figsize=(10, 8))

plt.subplot(3, 2, 1)
plt.stem(x1)
plt.title("Señal x1[n]")
plt.grid()

plt.subplot(3, 2, 2)
plt.stem(h1)
plt.title("Señal h1[n]")
plt.grid()

plt.subplot(3, 2, 3)
plt.stem(y1)
plt.title("Convolución y1[n]")
plt.grid()

plt.subplot(3, 2, 4)
plt.stem(x2)
plt.title("Señal x2[n]")
plt.grid()

plt.subplot(3, 2, 5)
plt.stem(h2)
plt.title("Señal h2[n]")
plt.grid()

plt.subplot(3, 2, 6)
plt.stem(y2)
plt.title("Convolución y2[n]")
plt.grid()

plt.tight_layout()
plt.show()

# Definir parámetros
Fs = 1 / (1.25e-3)  # Frecuencia de muestreo
Ts = 1 / Fs  # Período de muestreo
n = np.arange(0, 9)  # Vector de tiempo discreto

# Definir señales
x1 = np.cos(2 * np.pi * 100 * n * Ts)
x2 = np.sin(2 * np.pi * 100 * n * Ts)

# Calcular la correlación cruzada
corr = np.correlate(x1, x2, mode='full')

# Graficar señales y su correlación
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.stem(n, x1)
plt.title("Señal x1[n] = cos(2π100nTs)")
plt.grid()

plt.subplot(3, 1, 2)
plt.stem(n, x2)
plt.title("Señal x2[n] = sin(2π100nTs)")
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(range(-len(n) + 1, len(n)), corr)
plt.title("Correlación cruzada entre x1[n] y x2[n]")
plt.grid()

plt.tight_layout()
plt.show()



# Cargar datos del archivo .dat
file_path =r"C:\Users\juany\OneDrive\Escritorio\LabSeñales\Lab2\01.dat"
num_channels = 2  # Dos canales en la señal
Fs = 360  # Frecuencia de muestreo en Hz
Ts = 1 / Fs  # Período de muestreo

# Leer datos binarios
signal = np.fromfile(file_path, dtype=np.int16).reshape(-1, num_channels)
N = len(signal)
t = np.arange(N) / Fs  # Eje de tiempo

# Calcular estadísticos descriptivos
mean_signal = np.mean(signal, axis=0)
median_signal = np.median(signal, axis=0)
std_signal = np.std(signal, axis=0)
min_signal = np.min(signal, axis=0)
max_signal = np.max(signal, axis=0)

# Aplicar transformada de Fourier
frequencies = fftfreq(N, Ts)
spectrum = np.abs(fft(signal, axis=0))

# Calcular densidad espectral de potencia (PSD)
freqs, psd_ch1 = welch(signal[:, 0], Fs, nperseg=1024)
freqs, psd_ch2 = welch(signal[:, 1], Fs, nperseg=1024)

# Estadísticos en función de la frecuencia
mean_freq = np.sum(frequencies[:, None] * spectrum, axis=0) / np.sum(spectrum, axis=0)
median_freq = frequencies[np.argmax(np.cumsum(spectrum, axis=0) >= np.sum(spectrum, axis=0) / 2, axis=0)]
std_freq = np.sqrt(np.sum((frequencies[:, None] - mean_freq) ** 2 * spectrum, axis=0) / np.sum(spectrum, axis=0))

# Graficar señales
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, signal[:, 0], label="Canal 1")
plt.plot(t, signal[:, 1], label="Canal 2", alpha=0.7)
plt.title("Señal en el tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()

# Transformada de Fourier
plt.subplot(3, 1, 2)
plt.plot(frequencies[:N // 2], spectrum[:N // 2, 0], label="Canal 1")
plt.plot(frequencies[:N // 2], spectrum[:N // 2, 1], label="Canal 2", alpha=0.7)
plt.title("Transformada de Fourier")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()
plt.grid()

# Densidad espectral de potencia
plt.subplot(3, 1, 3)
plt.semilogy(freqs, psd_ch1, label="Canal 1")
plt.semilogy(freqs, psd_ch2, label="Canal 2", alpha=0.7)
plt.title("Densidad Espectral de Potencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("PSD")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# Histograma de la señal
plt.figure(figsize=(6, 4))
plt.hist(signal[:, 0], bins=30, alpha=0.7, label="Canal 1")
plt.hist(signal[:, 1], bins=30, alpha=0.7, label="Canal 2")
plt.title("Histograma de la señal")
plt.xlabel("Amplitud")
plt.ylabel("Frecuencia")
plt.legend()
plt.grid()
plt.show()

# Resultados de estadísticos
(mean_signal, median_signal, std_signal, min_signal, max_signal, mean_freq, median_freq, std_freq)

