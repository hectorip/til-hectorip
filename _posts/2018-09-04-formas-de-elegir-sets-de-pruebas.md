---
title: "Formas de elegir los sets de pruebas para modelos de ML"
date: 2018-09-04
author: Héctor Patricio
tags: ai machine-learning ml test-set
comments: true
excerpt: ""
<!-- header: -->
  <!-- image: http://res.cloudinary.com/hectorip/image/upload/v1535950811/residual_sixste.png -->
---

Para que un modelo de ML se comporte lo mejor posuble, se tiene que verificar su rendimiento
contra instancias de pruebas nunca usadas en el entrenamiento.

Para esto:
1. Se pueden conseguir más datos (bastante difícil normalmente)
2. Se puede dividir el conjunto de datos disponible en el conjunto de entrenamiento y el conjunto de pruebas

En todos lados donde he leído, siempre se inclinan por la sgunda opción, ya que no es normal que se
puedan pedir más datos de la nada. Además sería difícil de controlar.

Pero hacer la división no es tan fácil como parece, hay técnicas específicas para hacerlo. Lo normal es seprar entre **20% y el 30%** de los datos para el set de pruebas. **Y esos datos nunca tienen que pasar
por el modelo durante la etapa de entrenamiento**. 

¿Qué consideraciones hay que tener?

- **La selección tiene que se aleatoria.** Si se eligen datos secuenciales, podría elegirse una parte que
comparte características y se quitaría un parte importante de los datos de entrenamiento.

- **Una vez elegido un registro para el entrenamiento, no debe regresar al set de pruebas.** Para lograr
esto hay varias técnicas: diseñar un algoritmo que se asegure de que un registro sea identificable
para poder separarlo siempre, aunque nuestro conjunto de datos sea actualizado o confuigurar una semilla
para la selección aleatoria si el conjunto de datos no cambia.

Todo parecía más fácil desde afuera, jeje.