---
title: "Hug: API's rápidas con Python"
date: 2018-09-08
author: Héctor Patricio
tags: python hug api
comments: true
excerpt: "Una manera de hacer API's rápidamente con Python"
---

Yo creía que Flask era la manera más sencilla de hacer un proyecto web y sobre todo una API para pruebas.
A fin de cuentas, ¿qué puede ser más rápido que crear un archivo con las funciones mínimas necesarias,
unos decoradores y servir las respuestas formateadas como JSON? Pues lo que ofrece [hug](http://www.hug.rest/):
crear las funciones con decoradores y ni siquiera preocuparse por formatear la respuesta.


Lo siguiente ya es una API con todo y documentación:


```python
import hug

@hug.get()
def saludar(nombre: 'A quien saludar'):
    """
    Devuelve un saludo a la persona indicada
    """
    return {'saludo': 'Hola ' + nombre}
```


Ofrece documentación automática, versionamiento, está compilada con [Cython](http://cython.org/). La próxima API
que haga sin duda será hecha con **hug**.