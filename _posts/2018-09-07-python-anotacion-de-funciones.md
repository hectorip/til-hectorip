---
title: "Anotación de funciones en Python"
date: 2018-09-0
author: Héctor Patricio
tags: python function-annotation
comments: true
excerpt: "Anotación de funciones en Python"
---

Hoy encontré un código de Python con una sintaxis que no había visto nunca y se me hace rarísimo.

El código lucía algo así:


```python
def saludar(nombre: 'A quién saludar' = 'Héctor'):
    return 'Hola ' + nombre
```

Lo que viene después de los dos puntos del nombre del parámetro es un **function annotation**, que sirve para
almacenar metadatos acerca del parámetro en cuestión.

En algunos casos se usan como pistas para el tipo de dato esperado. La referencia completa está [aquí](https://www.python.org/dev/peps/pep-3107/).