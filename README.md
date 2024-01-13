# Car Color Recognition Project

## Descripción
Este proyecto está diseñado para identificar el color de los coches en imágenes utilizando técnicas de aprendizaje profundo. Se ha construido un modelo de clasificación utilizando una red neuronal convolucional (CNN) que puede distinguir entre varios colores como rojo, azul y negro.

## Estructura del Proyecto
El proyecto incluye los siguientes archivos clave:

- `Car_Color_Recognition.ipynb`: Un Jupyter Notebook que contiene todo el proceso de entrenamiento del modelo, incluida la carga de datos, el preprocesamiento, la definición del modelo, el entrenamiento y la evaluación, así como la visualización de los resultados.
- `format.py`: Un script de Python que se utiliza para formatear las imágenes del dataset a un tamaño uniforme y estructura requerida por el modelo.
- `splitter.py`: Un script de Python que divide el dataset en conjuntos de entrenamiento y validación.

## Cómo Usar

### Preparar el Entorno
Se recomienda crear un entorno virtual y instalar las dependencias necesarias siguiendo el orden de celdas. Requisitos previos mas abajo.

## Formatear el Dataset
Se puede usar cualquier dataset de imagenes de vehiculos clasificados por colores, despues utilizo las siguientes funciones para preparar los datos.
- Mi dataset usado en la bibliografia.<br>
Para formatear el dataset y prepararlo para el entrenamiento, ejecute:
```bash
python format.py
```
## Dividir el Dataset
Para dividir el dataset en conjuntos de entrenamiento y validación, ejecute:
```bash
python splitter.py
```
## Entrenamiento y Evaluación del Modelo
Para entrenar y evaluar el modelo, abra el notebook Car_Color_Recognition.ipynb en Jupyter y ejecute todas las celdas.<br>
En este repositorio incluyo algunas de las imagenes que he utilizado para la evaluación del modelo.
## Requisitos
- Python 3.8 o superior
- TensorFlow 2.x
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pillow

## Bibliografia 
Basado en el paper:<br>
https://arxiv.org/pdf/1510.07391.pdf<br>
Mi dataset:<br>
https://drive.google.com/file/d/1tdJ92Uhwp6-tWEqt19qcsZ7yoRb3dD8-/view?usp=sharing<br>
