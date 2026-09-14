# Race Engineer

El ingeniero de carrera responde preguntas aprobadas en inglés usando
reconocimiento de voz local, telemetría en vivo y reproducción de voz local.

## Estilo soportado

Haz preguntas cortas de contexto de carrera, por ejemplo:

- What is my position?
- What is my fuel?
- What is my lap time?
- What gear am I in?
- What is my speed?

La preview es determinística: las respuestas salen de patrones conocidos y
telemetría disponible, no de análisis libre en tiempo real.

## Voz

El reconocimiento y la reproducción de voz corren localmente. La app puede
necesitar preparar recursos locales antes de que el ingeniero esté listo.

Si no hay telemetría disponible, el ingeniero puede responder con un mensaje
breve de datos faltantes en lugar de inventar información.
