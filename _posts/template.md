---
title: "Medidas de comportamiento para evaluar modelos de regresión"
date: 2018-09-01
author: Héctor Patricio
tags: ai machine-learning regresión distancias(ml)
comments: true
excerpt: ""
header:
  image: http://res.cloudinary.com/hectorip/image/upload/v1535950811/residual_sixste.png
---

Después de entrenar o crear un modelo de regresión hay que evaluar que tan bien se comporta, es decir,
qué tan bueno es. Una forma es mediante la medición de los errores cometidos sobre un set de pruebas.

Uno de los más comunes es la **Raíz de la media del Error al cuadrado (Root Mean Square Error o RMSE)**,
que mide da en pocas palabras la desviación estándar de los errores que el modelo produce. Es decir, si
tenemos un modelo de regresión lineal con un RMSE de 10 unidades, si la característica que estamos
evaluando se comporta según la distribución normal, el 68% de los errores sería de máximo 10 unidades, mientras que el 95% de errores sería de máximo 20. Todavía estoy intentando entender completamente esto y aplicarlo.