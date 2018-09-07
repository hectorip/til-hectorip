---
title: "Colecciones útiles de Python"
date: 2018-09-06
author: Héctor Patricio
tags: python colecciones
comments: true
excerpt: "Colecciones útiles y poco conocidas de Python"
---

Por pura curiosidad ayer empecé a leer el libro [20 Python Libraries You Aren't Using](https://www.oreilly.com/programming/free/files/20-python-libraries-you-arent-using-but-should.pdf) y
empecé a descurbir que Python es mucho, mucho más grande de lo que pensaba.

Lo primero con lo que empieza es con el módulo `collections`. Ya me había enfrentado al problema de los
diccionarios ordenados, y los había usado un poco, pero una colección que me sorprendió muchi y quiero empezar a usar
es la tupla nombrada:

```python
from collections import namedtuple

T = namedtuple('llave1', 'llave2')

mis_valores = T(1, 2)

mis_valores.llave1 #. 1
mis_valores.llave2 #. 2

```

Se parece a un diccionario u objeto, con el rendimiento de una tupla. Y es completamente compatible con la tupla
normal:

```python
(v1, v2) = mis_valores
```
Espero me siga dejando tanto como hasta ahora este libro.