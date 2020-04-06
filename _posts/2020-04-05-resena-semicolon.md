---
title: ""
date: 2020-04-05
author: Héctor Patricio
tags: reseña libro semicolon gramática
comments: true
excerpt: "Uso de Hexdump"
header:
  image: 
---

**Hexdump** es una herramienta que permite examinar el contenido de un archivo en sistemas Unix mediante mostrar explícitamente todos los bytes que contiene representados con su valor hexadecimal.

Por ejemplo, imagina que tienes un archivo llamado `hello.txt` que tiene como contenido "hello". El comando `hexdump hello.txt` mostrará el contenido en pares de carácteres hexadecimales.

```
0000000 68 65 6c 6c 6f 0a
0000006

```

La primera columna significa el byte en el que la línea actual comienza (el _offset_). Los demás valores son las representaciones hexadecimales de la cadena "hello" más el salto del línea (`0a` o `\n`).

Si queremos ver a qué valores corresponde cada byte podemos usar la bandera `-C` que pone el contenido al lado. Si un carácter no tiene representación visual en ASCII usará un "." (punto).

```
00000000  68 65 6c 6c 6f 0a                    |hello.|
00000006
```

Esta herramienta es muy muy útil cuando existen carácteres que tu editor de textos no puede mostrar pero te están dando algún tipo de problemas. Por ejemplo el BOM de un CSV.
