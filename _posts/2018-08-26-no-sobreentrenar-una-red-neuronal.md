---
title: "Entrenar por más épocas una red neuronal no siempre resulta mejor"
date: 2018-08-26
author: Héctor Patricio
tags: ai redes-neuronales
comments: true
---

![Relojes](http://res.cloudinary.com/hectorip/image/upload/c_scale,w_703/v1535779302/jon-tyson-771694-unsplash_wnjc6n.jpg)

En un ejercicio que nos dejaron durante la clase de la RIIAA, para detectar puntos de datos
o registros de partículas subatómicas que correspondieran al Bosón de Higgs con una confianza de
más de 4 sigmas, nos enseñaron a crear una red neuronal que se entrena por la cantidad de tiempo
determinado por el programador, cada entrenamiento se llama **una época (epoch)**.

Después de hacer muchos intentos y por expereincia propia (entrenando hasta por 100 épocas la red neuronal),
comprobé algo que nos mostraron durante la clase y con lo que hay que tener cuidado a la hora de entrenar
la red neuronal: **entrenarla por más tiempo no significa que se comportará mejor, pero entrenarla menos tiempo
del debido tampoco es una solución óptima.**. La gráfica siguiente lo describe mejor:

![Errores en una red neuronal sobre-entrenada](https://i.stack.imgur.com/HTYZW.png)

El punto es, para cada set de datos, encontrar el número de épocas que hay que entrenar la red para llegar
al lugar de la gráfica que está antes que se empiece mover en zig-zag de arriba hacia abajo.