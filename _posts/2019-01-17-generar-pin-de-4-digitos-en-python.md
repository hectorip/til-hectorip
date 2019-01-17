---
title: "Generar pin de 4 dígitos en python"
date: 2019-01-17
author: Héctor Patricio
tags:
comments: true
excerpt: "Un pequeño snippet para genera un pin de 4 dígitos en Python"
header:
  image: #image
---

Tenía que generar un pequeño número para una aplicación, aquí el snippet por si
algún día lo necesitas, con longitud personalizada.

```python
from random import randint

def generate_pin(length=4):
  upper_limit = 10 ** length
  pin = randint(0, upper_limit-1)
  return "{:04d}".format(pin)
```