---
title: "Mongo no crea DB hasta que existe una colección"
date: 2018-09-05
author: Héctor Patricio
tags: mongo db db-admin
comments: true
excerpt: "MongoDB es engañoso"
---

Las lecciones de hoy son más o menos claras:

1. No existe una manera de crear bases de datos como tal en Mongo. Para crearlas, hay que usar
el comando `use nombre_de_db` y después crear una colección. Si no se crea la colección, la base de datos
no existirá por si misma.

2. Para hacer autenticación con un usuario indicando la base da datos, el usuario **tiene que estar creado en esa base de datos**, no importando que sea un usuario administrador que tenga permisos de lectura y escritura sobre todas las bases de datos.


Esto me costó media hora de mi día, espero ahorrársela a alguien.