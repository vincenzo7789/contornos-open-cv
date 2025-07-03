# Detector de Color en Espacio LAB con OpenCV

**Detector interactivo de colores utilizando la cámara web y el espacio de color LAB.**  
Ideal para aplicaciones de visión por computadora donde se requiere detección precisa de color bajo distintas condiciones de iluminación.

## Contenido

- [ Requisitos](#-requisitos)
- [ Instalación](#️-instalación)
- [ Uso](#️-uso)
- [ Configuración Interactiva](#️-configuración-interactiva)
- [ Visualización](#️-visualización)
- [ Tecnología](#-tecnología)
- [ Licencia](#-licencia)

## Requisitos

- Python 3.x  
- `opencv-python` >= 4.5  
- `numpy` >= 1.20

## Instalación

```bash
git clone https://github.com/tu-usuario/detector-lab.git
cd detector-lab
pip install -r requirements.txt
```

##  Uso
Ejecuta el script principal:
```bash
python detector_lab.py
```
Presiona la tecla `q` para salir de la aplicación.

 ##  Configuración Interactiva

Desde la ventana Ajustes LAB, puedes modificar:

Rango de color LAB:
- `L_min` / `L_max`: componente de luminosidad (L)
- `a_min` / `a_max`: componente de color verde-rojo (a)
- `b_min` / `b_max`: componente de color azul-amarillo 


## Operaciones morfológicas
- `Kernel`: tamaño del núcleo utilizado
- `Erosiones`: cantidad de erosiones aplicadas
- `Dilataciones`: cantidad de dilataciones aplicadas


## Visualización
Se muestran tres ventanas en tiempo real:
- `Frame Original`: imagen capturada de la cámara
- `Máscara LAB`: máscara binaria del color detectado
- `Azul Detectado`: resultado de aplicar la máscara al frame original

## Tecnología
- `OpenCV`: detección y manipulación de imágenes en tiempo real
- `Espacio LAB`: mejor desempeño para segmentar colores en condiciones de luz variable
- `Interfaz con Trackbars`: modificación dinámica de parámetros sin reiniciar el programa

## Licencias 

Este proyecto utiliza una licencia abierta (especifica aquí si es MIT, GPL, etc).















