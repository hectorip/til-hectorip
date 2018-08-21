---
title: "Agregar Disqus como sistema de comentarios a Jekyll en GitHub Pages"
date: 2018-08-19
author: Héctor Patricio
tags: github, disqus, jekyll, github-pages
comments: true
---

Una de las primeras tareas para este blog fue agregar comentarios ya que Jekyll viene
sin ninguna forma de hacerlo naturalmente. Y la forma más fácil es através de [Disqus](https://disqus.com/), una plataforma especializada en comentarios.

En la [documentación](https://disqus.com/admin/install/platforms/jekyll/) encontramos como hacerlo con Jekyll puro, pero en el caso de GH Pages hay que seguir un proceso un poco diferente ya que el proyecto no tiene la misma estructura que Jekyll normal.

Instalación:

1. Crear la carpeta `_layouts` y dentro de ella crear el archivo post.html, con la estructura básica para mostrar un post (recomiendo buscar el archivo en el repo de tu tema y coipiarlo). En mi caso era el siguiente:
{% raw %}
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
2. Después de esto se pueden seguir las instrucciones de la documentación de Disqus. Que en pocas palabras es agregar el siguiente código (con tus valores propios) al final del archivo:

```html
{% if page.comments %}
<div id="disqus_thread"></div>
<script>
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://TU_URL_PERSONALIZADA.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
{% endif %}

```
{% endraw %}


El código se puede ver en esta mismo repo, en `_layouts/post.html`.
