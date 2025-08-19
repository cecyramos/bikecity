
# BIKECITY

Sistema automatizado para la gestión de reservas y renta de bicicletas urbanas.

## Descripción

Este proyecto resuelve los problemas de reservas duplicadas, cobros incorrectos y falta de control sobre bicicletas disponibles, mediante un sistema que:

- Registra bicicletas disponibles para renta.
- Gestiona reservas evitando conflictos de horario.
- Aplica cobros correctos según la duración del uso.
- Controla el estado de cada bicicleta.

## Estructura del proyecto

- `bicicleta.py`: Clase y lógica para bicicletas.
- `reserva.py`: Clase y lógica para reservas.
- `main.py`: Menú principal y flujo de la aplicación.

## Ejecución

Ejecuta el sistema con:

```sh
python main.py
```

## Requerimientos

- Python 3.x

## Manejo de excepciones

El sistema utiliza excepciones personalizadas y bloques try/except para validar entradas y evitar errores comunes.

## Autores

Equipo BIKECITY Bootcamp Python

Ejercicio grupal
Contexto

Tres amigos han creado un emprendimiento llamado "BIKECITY", un servicio de renta de bicicletas urbanas. Los clientes deben llamar o enviar mensajes a los dueños para reservar una bicicleta, pero el sistema manual que utilizan ha generado los siguientes problemas:

Reservas duplicadas por falta de sincronización entre los socios.

Clientes que no recogen las bicicletas reservadas, generando pérdidas.

Cobros incorrectos debido a errores en los cálculos manuales.

Falta de registro sobre las bicicletas disponibles y su estado.

Solución

Se necesita desarrollar un sistema automatizado que permita:

Registrar bicicletas disponibles para renta.

Gestionar reservas evitando conflictos de horario.

Aplicar cobros correctos según la duración del uso.

Controlar el estado de cada bicicleta para evitar pérdidas o mal uso.

Requerimiento

Paso 1: Conceptualización y Análisis 
Cada equipo debe investigar y responder en un documento las siguientes preguntas:

¿Qué es una excepción en programación y por qué es importante manejarla correctamente?

¿Cuáles son los tipos de excepciones más comunes?

¿Cómo funciona la sentencia try/except y cuándo se debe utilizar?

¿Cómo se pueden capturar múltiples excepciones en un solo bloque de código?

¿Qué es el uso de raise en Python y cómo se utiliza para generar excepciones en validaciones?

¿Cómo se pueden definir excepciones personalizadas y en qué casos sería útil?

¿Cuál es la función de finally en el manejo de excepciones?

¿Cuáles son algunas acciones de limpieza que deben ejecutarse después de un proceso que puede generar errores?

Paso 2: Implementación en Código 
Cada equipo debe implementar un código en Python que simule el sistema de reservas y manejo de bicicletas, utilizando los conceptos de manejo de excepciones.

Tareas del equipo:

Crear clases para representar bicicletas y reservas.

Aplicar try/except para manejar errores en el sistema.

Capturar múltiples excepciones en el mismo bloque de código.

Usar raise para generar excepciones cuando haya errores en las reservas.

Definir una excepción personalizada para manejar casos específicos.

Usar finally para acciones de limpieza, como cerrar conexiones o registrar información en logs.

Paso 3: Documentación y Entrega
El equipo debe entregar un archivo comprimido (.RAR o .ZIP) que contenga:

Documento con las respuestas del análisis.

Código Python con el sistema de reservas y manejo de excepciones.

Duración: 1 Jornada de Clases.