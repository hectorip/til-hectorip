---
title: "Temas de Jekyll en GitHub Pages"
date: 2018-08-20
author: Héctor Patricio
tags: github ghpages jekyll github-pages
comments: true
---

Buscando la manera de configurar un tema que no estuviera en la lista oficial de 
temas de Jekyll para la instalación default de GitHub Pages, encontré una
[página de la documentación](https://blog.github.com/2017-11-29-use-any-theme-with-github-pages/)
que mencionaba que se podría configurar cualquier tema a partir del 2017, con la llave de
configuración `remote_theme: usuario/repo`.


Sin embargo, al probar y leer la documentación de varios como [jasper2](https://github.com/jekyller/jasper2) y [Type on Strap](https://github.com/Sylhare/Type-on-Strap), me di cuenta de que aunque puede ser que el tema visual esté soportado (CSS, layouts y JS), la mayoría de los temas se complementa con otros plugins no soportados por la instalación default de GH Pages, por lo que no se pueden instalar directamente, para hacerlo hay que hacer la generación del sitio por separado y subir el sitio generado al repositorio, de preferencia al branch gh-pages. So sad.