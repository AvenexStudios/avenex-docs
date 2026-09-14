# Race Engineer

El ingeniero de carrera responde preguntas aprobadas en inglés usando
reconocimiento de voz local, telemetría en vivo y reproducción de voz local.

## Estilo soportado

Haz preguntas cortas de contexto de carrera, por ejemplo:

| Tema | Preguntas de ejemplo |
| ---- | -------------------- |
| Posición | What is my position? Where am I? |
| Gaps | What is the gap ahead? What is the gap behind? |
| Sesión | How many laps left? How long left? |
| Ritmo | What was my last lap? What is my best lap? What lap am I on? |
| Combustible | How much fuel? How many laps of fuel do I have left? |
| Estado del auto | What gear am I in? What is my speed? What are my RPM? |
| Condiciones | What is the track temperature? What is the air temperature? |
| Controles | Say again. Repeat that. Keep quiet. Keep me informed. |

La preview es determinística: las respuestas salen de patrones conocidos y
telemetría disponible, no de análisis libre en tiempo real.

Algunas preguntas dependen de campos de telemetría que pueden no estar
disponibles en todas las sesiones. Cuando falta información, el ingeniero
debería decir que no tiene ese dato en lugar de inventarlo.

## Voz

El reconocimiento y la reproducción de voz corren localmente. La app puede
necesitar preparar recursos locales antes de que el ingeniero esté listo.

Si no hay telemetría disponible, el ingeniero puede responder con un mensaje
breve de datos faltantes en lugar de inventar información.
