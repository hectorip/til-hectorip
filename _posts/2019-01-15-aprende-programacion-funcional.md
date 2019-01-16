---
title: "Aprende programación funcional #1 -> ¿Qué es?"
date: 2019-01-15
author: Héctor Patricio
tags:
comments: true
excerpt: "¿Qué es la programación funcional y cómo puedes aprenderla? En este post lo explico después de una larga investigación"
header:
  image: 
---

La programación funcional ha sido un tema recurrente en el mundo de desarrollo en los últimos años que ha llamado la atención
por todos los mitos y cosas difíciles de entender alrededor de ella.

No me considero un super experto en programación funcional pero en este post quiero compartir lo que he aprendido, sobre
todo a través de programar en Elixir e investigar un montón las dudas que he tenido. Este es el primero de una serie de posts
en el que quiero enseñar lo que sé acerca de este paradigma-estilo de programación para solidificarlo en mi mente.

Así que empecemos.

## ¿Qué es la programación funcional?

En general, no hay una deficinición aceptada por todos y cada que buscas en google el término salen un montón de definciones y palabras raras que 
sólo los matemáticos o los progrmadores funcionales medio entienden.
Muchos la relacionan con el paralelismo, la inmutabilidad, la recursividad, MapReduce y otras cosas más, que aunque sí tienen cierta relación
con los lenguajes funcionales actuales, no es cierto que todas características esenciales o que se tenga hablar de esto antes de comprender la programación
funcional.

Entre todo lo que busqué encontré una definición que siento que satisface:

> Estilo de programación que se enfoca 1) en las funciones puras y 2) valores inmutables. En los lenguajes que la soportan, casi todo es una expresión (tiene un valor) o puede considerarse una función.

Todas las demás características que se le atribuyen o con las que se relaciona están derivadas de estas dos. Pero para entender mejor
el estilo, tenemos que definir correctamente estas dos características.

### Funciones puras

Si ya programas, probablemente conozcas bien el concepto de función: una pedazo de código encapsulado bajo un nombre que puede ser
ejecutado bajo demanda, aislado del contexto externo que lo solicita y que por lo tanto puede enviar(valor de retorno) o recibir(parámetros) información de este.

Una función pura es algo similar con dos restricciones:

1. No toma valores del contexto (ni de ninguna otra parte) que no hayan sido pasados como parámetros explícitamente. Por ejemplo, una función no puede recibir un valor como referencia y modificarlo desde el interior de la función.
2. No modifica datos fuera de ella (efectos secundarios).

<!-- Entonces una función pura es aquella que no tiene efectos secundarios -->
Estas dos características hacen que una función pura sea más fácil de entender y mantener. Permiten características como el "cacheo" (memoization) de valores
y habilitan la transferencia referencial y muchas otras cosas relacionadas con la programación funcional.

Voy a dedicar un artículo completo más adelante a explicar cómo las funciones sin efectos secundarios habilitan a los programadores para hacer mejores programas.

### Valores inmutables

Esto sencillamente quiere decir que una vez declarado un valor y creado en la memoria, no puede ser modificado. Se pueden crear nuevos valores
a partir de operaciones con este, pero nunca va a cambiar el valor original. Esto también merece su propio artículo.

## Conclusión

Eso es básicamente la programación funcional. En el siguiente artículo explicaré con más detalle, ahora sí, las carácterísitcas que simpre salen a
discusión cuando hablamos de ella, y se relacionarán con las dos características principales que mencionamos.
