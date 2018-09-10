---
title: "Paquetes de Go para peticiones HTTP"
date: 2018-09-09
author: Héctor Patricio
tags: golang http
comments: true
excerpt: "Algunas opciones extra a la biblioteca estándar para peticiones HTTP"
---

Desde que empecé a programar en Go me di cuenta de que tiene una biblioteca estándar bastante buena y
completa. Pero algo de lo que no me gusta hacer son peticiones web con el paquete que tiene incluído:
`http`.

Por eso, hoy mismo que tenía que hacer peticiones para un programa que estoy desarrollando, me encontré
con dos por lo menos, aunque no he tenido tiempo de implementar ninguna:

1. [GoRequest](https://github.com/parnurzeal/gorequest). Inspirada en un paquete de NodeJS.
2. [grequests](https://github.com/levigross/grequests). Dicen que es un porte de la `requests` de Python.