---
title: "Agregar Disqus como sistema de comentarios a Jekyll en GitHub Pages"
date: 2018-08-19
author: Héctor Patricio
tags: github, disqus, jekyll, github-pages
comments: true
---

# Agregar Disqus como sistema de comentarios a Jekyll en GitHub Pages


Una de las primeras tareas para este blog fue agregar comentarios ya que Jekyll viene
sin ninguna forma de hacerlo naturalmente. Y la forma más fácil es através de (https://disqus.com/profile/login/)[Disqus] una plataforma especializada en comentarios.

En la (https://disqus.com/admin/install/platforms/jekyll/)[documentación] viene como hacerlo con Jekyll puro, pero en el caso de GH Pages hay que seguir un proceso un poco diferente ya que el proyecto no tiene la misma estructura que Jekyll normal.

Instalación:

1. Crear la carpeta \_layouts y dentro de ella crear el archivo post.html, con la estructura básica para mostrar un post (recomiendo buscar el archivo en el repo de tu tema y coipiarlo). En mi caso era el siguiente:

```html
---
layout: default
---

<small>{{ page.date | date: "%-d %B %Y" }}</small>
<h1>{{ page.title }}</h1>

<p class="view">by {{ page.author | default: site.author }}</p>

{{content}}

{% if page.tags %}
  <small>tags: <em>{{ page.tags | join: "</em> - <em>" }}</em></small>
{% endif %}
```
