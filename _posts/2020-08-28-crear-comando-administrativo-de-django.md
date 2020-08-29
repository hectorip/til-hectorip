---
title: "Cómo crear comandos administrativos de Django"
date: 2018-09-00
author: Héctor Patricio
tags: django python tools
comments: true
excerpt: "Instrucciones sencillas para crear un comando que corra con el manage.py de Django."
---

Hoy tuve que hacer un comando administrativo de Django para crear automáticamente unos registros en la base de datos que son variables y por lo que no podían ser fixtures.

Los he hecho varias veces pero cada vez que me toca hacer uno tengo que volver a Googlear cómo hacerlo así que escribo esto para mi en el futuro y para que se asiente mejor lo que aprendí (recordé) hoy.

## El archivo

Dentro de la carpeta aplicación que creas que es la más adecuada para contener el comando crea una carpeta llamada `management` y dentro una llamada `commands`.

Ahí adentro crea el archivo que contendrá el código de tu comando. **El nombre del archivo es el nombre del comando**. O sea, si tu archivo se llama "run_magic_code" lo tendrás que correr como: `python manage.py run_magic_code`.

## El código

Este es el único código que necesitas:

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Descripción de tu comando y opciones de configuración"

    def handle(self, *args, **options):
      self.stdout.write("Éxito, corriendo", self.style.SUCCESS)
```

Ahora rellena `handle` con tu código específico. Este es como cualquier otro archivo del proyecto de Django, por lo que puedes importar tus los settings, tus modelos, o lo que necesites.

La última línea no es necesaria pero es un ejemplo de cómo escribir un mensaje formateado como texto que quiere señalizar que algo salió bien. Esto será muy útil si quieres dar detalles de cómo va el proceso.

Lo demás lo puedes leer aquí (en inglés): [Writing custom django-admin Commands](https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/)

Y aquí un tutorial un poco más extenso en español: [Comandos de Gestión de Django](https://sodocumentation.net/es/django/topic/1661/comandos-de-gestion).
