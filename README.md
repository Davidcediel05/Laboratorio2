# Laboratorio 2
## Convolucion, Correlacion y Transformacion.
### Descripcion 
<p>
En este proyecto se busca reconocer las operaciones entre señales, Es importante tener en cuenta que la convolución y la correlación son operaciones matematicas primordiales en el análisis de señales. En este laboratorio, utilizaremos estas herramientas matemáticas para comprender su aplicación en el procesamiento digital de señales. 

</p>

#### Convolucion
<p>
La convolución es una operación matemática que combina dos funciones para describir la superposición entre ambas. En el procesamiento de señales se emplea para conocer que le sucede a una señal despues de pasar por un determinado dispositivo, detectan patrones que despues clasifican.
La convolucion define como un sistema modifica su señal de entrada utilizando su respuesta al impulso, es muy util para observar los sistemas lineales e invariantes en el tiempo. su principal funcion es combinar señales para describir sistemas. 
   
   - Para la funcion X (n)=[1,0,0,0,9,7,1,3,6,4] y H(n)=[5,6,0,0,6,1,6]

![image](https://github.com/user-attachments/assets/e805c1e4-1338-4bb0-a83e-253e18b22434)
![image](https://github.com/user-attachments/assets/f3854a79-c290-470d-8498-688884937d94)
![image](https://github.com/user-attachments/assets/c94812bc-a9ba-4021-bc34-b5553adeb9d0)

   - Para la funcion  X(n)=[1,0,2,5,4,6,1,2,4,5] y H(n)=[5,6,0,0,6,1,1].

![image](https://github.com/user-attachments/assets/fbf02378-4bff-4958-9f1c-56d1ae458709)
![image](https://github.com/user-attachments/assets/df538c97-d4b2-42da-b779-d0d6c04b8592)
![image](https://github.com/user-attachments/assets/49a80bf7-a9ca-4e20-9552-2b931b2d83ba)

</p>

#### Correlacion. 

<p>
La correlacion se encarga de medir la similitud entre señales, indica que tanto se parece una señal a la otra mientras una se desplaza respecto a la otra.
Hay dos tipos de correlacion.

-Autocorrelacion: Mide la periodicidad de una señal por lo tanto es la correlacion de una señal consigo misma.

-Correlacion cruzada: Se encarga de medir similitudes entre señales diferentes.

</p>


**Implementación en el Código:**

`def calcular_snr(señal_ori, señal_ruido):

    potencia_señal = np.mean(señal_ori ** 2)
    
    ruido = señal_ruido - señal_ori
    
    potencia_ruido = np.mean(ruido ** 2)
    
    snr = 10 * np.log10(potencia_señal / potencia_ruido)
    
    return snr`
    




</p>


#### Transformada de Fourier.
<P>
Una transformacion es una operacion que convierte una señal desde un dominio a otro dominio, la transformada de fourier convierte una señal del dominio del tiempo hacie el dominio de la frecuencia. Lo cual permite analizar las señales en dominios alternativos lo cual permite identificar las caracteristicas como frecuencias.
    


En la grafica se logra observar la aparición de picos abruptos que ocurren de manera constante a lo largo de la señal, su SNR (-9.73dB) nos indica que el ruido influye en la claridad de la señal original.
**Implementación en el Código:**
`def ruido_impulso(señal, porcentaje=0.05):

    señal_ruidosa = señal.copy()
    
    num_muestras = int(len(señal) * porcentaje)
    
    indices = np.random.choice(len(señal), num_muestras, replace=False)
    
    señal_ruidosa[indices] = np.max(señal) * np.random.choice([-1, 1], size=num_muestras)
    
    graficar_señales(tiempo, señal, señal_ruidosa, "Ruido de Impulso", calcular_snr(señal, señal_ruidosa))`
    
Donde:
-	Se selecciona un 5% de la señal (por defecto).
-	Se eligen posiciones aleatorias en la señal.
-	Se reemplazan con valores máximos o mínimos.
-	Se grafica la señal con ruido.

</p>





</p>

### Análisis Estadístico de la Señal

<p>
El análisis estadístico de la señal EMG permite extraer información relevante sobre su comportamiento, lo que es fundamental para diversas aplicaciones biomédicas. Algunos de los aspectos analizados incluyen:
</p>

- **La Media:**  De una señal es una medida fundamental que proporciona información sobre el valor promedio de los datos. 
- **Desviación estándar:** La desviación estándar de una señal es una medida de variabilidad de los datos.
- **Coeficiente de variación:** Analiza la variabilidad relativa de las señales, en aplicaciones como la electromiografía, donde es importante comparar señales en diferentes condiciones.
  
![Metricas](https://github.com/user-attachments/assets/d5c5d173-16dc-4a44-a0e9-88008b335190)

#### Estas medidas en señales EMG, nos permite:
- Evaluar la amplitud de la señal.
- Detectar ruido o artefactos.
- Comparar la actividad muscular entre diferentes canales o condiciones.
- Analizar la calidad de la señal.

**Histograma:** Es una herramienta grafica que nos permite analizar las propiedades estadísticas y visuales de una señal, para su procesamiento y mejora.
- Visualizar la distribución de amplitudes
- Identificar características estadísticas
- Detectar ruido o anomalías
- Análisis de contraste en imágenes
- Compresión de datos
- Diseño de filtros

![Histograma](https://github.com/user-attachments/assets/8c307ff4-5c97-4711-aa62-69623eccfd08)

<p>
  En la grafica podemos observar que en la actividad muscular se presentan valores positivos mas frecuentes lo cual sugiere que hubo contracción muscular durante la medición, es evidente que el pico es muy pronunciado, lo cual indica que la señal tiene una buena calidad.
</p>

### Requisitos
<p>
Para ejecutar el código, es necesario instalar Python y las siguientes librerías:
  
- wfdb
- numpy
- matplotlib
- scipy
  
Tener instalado un compilador, que para este caso se utilizo spyder.  
</p>

### Caracteristicas principales
- Lectura de señales EMG: Utiliza la biblioteca wfdb para leer señales EMG desde un archivo.
- Visualización de señales: Grafica las señales EMG en el dominio del tiempo.
- Cálculo de métricas estadísticas: Calcula la media, desviación estándar, coeficiente de variación y genera histogramas con funciones de densidad de probabilidad (PDF).
- Agregar ruido: Permite agregar ruido gaussiano, ruido de impulso y ruido tipo artefacto a la señal.
- Cálculo de SNR: Calcula la relación señal-ruido (SNR) después de agregar ruido.

### Estructura del proyecto
- Lab1.py: Lee y visualiza la señal EMG desde un archivo
- LABfinal.py: Versión optimizada del procesamiento de señales EMG.
- Pruebaruido.py: Genera ruido aleatorio y analiza su comportamiento en el dominio de la frecuencia.
- emg_healthy.dat y emg_healthy.hea: Archivos de datos de la señal EMG.
- Lab1s.docx: Documento con información del laboratorio.

### Ejecución

- Asegúrate de que los archivos de datos están en la misma carpeta que los scripts.
-	Ejecuta Lab1.py o LABfinal.py para analizar la señal:
- python Lab1.py
  Para probar la simulación de ruido, ejecuta:
  
`python Pruebaruido.py`


### Conclusión
<p>
Este proyecto nos permite identificar las métricas estadísticas de una señal de EMG en condiciones normales, para posteriormente analizar el comportamiento de esta señal agregando diferentes tipos de ruidos y con ello calcular su SNR lo cual nos ayuda a comprender el fundamento y el impacto de estos ruido.
</p>

### Bibliografia

- Sartori, P., Rozowykniat, M., Siviero, L., Barba, G., Peña, A., Mayol, N., Acosta, D., Castro, J., & Ortiz, A. (2015). Artefactos y artificios frecuentes en tomografía computada y resonancia magnética. Revista Argentina de Radiología / Argentinian Journal Of Radiology, 79(4), 192-204. https://doi.org/10.1016/j.rard.2015.04.005
- Svantek. (2023, 27 septiembre). Ruido de impulso | ¿Cómo medir? | Consultores Svantek. SVANTEK - Sound And Vibration. https://svantek.com/es/servicios/ruido-de-impulso/#:~:text=El%20ruido%20de%20impulso%20se,inferior%20a%201%20segundo)%C2%BB.
- Learn Statistics Easily. (2024, 24 julio). Qué es: Ruido Gaussiano - APRENDE ESTADÍSTICAS FÁCILMENTE. LEARN STATISTICS EASILY. https://es.statisticseasily.com/glossario/what-is-gaussian-noise/


### Licencia

Este proyecto es de uso académico y educativo.

### Contacto
<p>
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:
</p>

- **Nombre:** [Juan David Cediel Farfan][Juan Yael Barriga Roa]
- **Email:** [est.juand.cediel@unimilitar.edu.co][est.juan.barriga@unimilitar.edu.co]
- **GitHub:** [David05Cediel][JuanYBR]

