---
title: "Dividir un archivo en dos en terminal de Linux y Mac"
date: 2018-09-03
author: Héctor Patricio
tags: bash split trabajo-con-archivos archivos-de-texto
comments: true
excerpt: ""
<!-- header:
  image: http://res.cloudinary.com/hectorip/image/upload/v1535950811/residual_sixste.png -->
---

Hoy me pidieron dividir un CSV de más de 1M de líneas en por lo menos dos archivos, para poderlo
manejar mejor.

La primera forma que se me ocurrió fue con **head** y **tail**, pero no sabía que existe un programa
de los sistemas POSIX que lo hace súper fácil:

```bash
split -l numero_de_lineas nombre_del_archivo
```

Es decir, si mi archivo a dividir se llama "datos.csv", tiene 10000 líneas y quiero obtener dos archivos
de 5000 líneas, el comando sería:

```bash
split -l 5000 datos.csv
```

Este comando producirá en el mismo directorio dos archivos nombrados `xaa` y `xab` conteniendo cada uno
5000 líneas, dejando el archivo original intacto.

Se producirán tantos archivos como divisiones sean posibles.