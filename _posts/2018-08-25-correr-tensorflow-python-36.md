---
title: "Correr TensorFlow y TensorFlow Hub"
date: 2018-08-24
author: Héctor Patricio
tags: deep-learning ai tensorflow tensorflow-hub
comments: true
---

![TensorFlow Logo](http://res.cloudinary.com/hectorip/image/upload/c_scale,w_700/v1535694725/Tensorflow_logo.svg_vkbzhz.png)


Entre las cosas que se mencionaron ayer bastante y que he estado esuchando muchísimo
en el mundo del análisis de datos es [TensorFlow](https://www.tensorflow.org/) que lo entiendo,
aunque tal vez mi definición no sea tan precisa, como un framework de cálculo numérico acelerado
por GPU o TPU(hardware especializado en operaciones matemáticas) enfocado en el aprendizaje automático,
permitiendo así ser más eficientes par generar y entrenar modelos.

Uno de los ejercicios consistía en correr un hojo de [Google Colab](https://colab.research.google.com/) con unos
ejercicios de TensorFlow y Keras, pero esto no me dejó completamente satisfecho y quise correr el ejercicio en
mi propia máquina (más bien, el ejericio de la página de TensorFlowHub). Yo sólo tenía python 3.7 en mi máquina
y al intentar instalar TF me decía que todo había ido bien pero al intentar correr un programa que usara la librería no se podía encontrar.

Después de batallar bastantes horas encontré la solución, que comparto a continuación:

1. La versión actual de TF sólo corre en Python 3.6 (finales de Ago de 2018), se encuentra un versión en pip que
se descarga pero no es capaz de correr.
2. Se tiene que instalar una versión que se descarga directamente de con Google:

```bash

pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.10.1-py3-none-any.whl
```

El link de la versión más recientemente cambiará. De momento me queda la lección de no creer que porque algo
viene de Google, no fallará.


