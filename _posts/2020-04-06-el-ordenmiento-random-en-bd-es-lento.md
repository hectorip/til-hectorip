---
title: "El ordenamiento aleatorio (order by '?') en bases de datos relacionales no es recomendable"
date: 2020-04-05
author: Héctor Patricio
tags: sql bases-de-datos
comments: true
excerpt: "Por qué el ordenamiento aleatorio en base de datos es lento"
---

Buscando una solución para seleccionar un registro aleatorio en un modelo de Django, busqué si había forma de ordenar una colección de manera aleatoria y después seleccionar el primero de la colección.

Resulta que ordenar de esta manera es una muy mala solución, por lo menos desde la base de datos. Aquí hay una muy buena explicación: [StackOverflow](https://stackoverflow.com/questions/1731346/how-to-get-two-random-records-with-django/6405601#6405601).

El resumen: el motor de bases de datos tiene que crear una tabla temporal y si tienes un montón de registros vas a matar a tu servidor en poco tiempo, sobre todo si es una operación recurrente.

La mejor forma de hacerlo es:

1. Contar los registros
2. Seleccionar un entero aleatorio entre 0 y el número de registros
3. Traer ese registro en específico
