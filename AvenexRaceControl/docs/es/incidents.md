# Incidentes y severidad

Avenex cuenta participación en accidentes, no culpabilidad ni intención.

## Qué cuenta
Un incidente requiere evidencia de contacto que involucre al piloto. Una
pasada cercana, que otro auto frene o un cambio de velocidad por sí solo no
deben contar como choque. Varias observaciones del mismo accidente se agrupan
para no cobrar cada una por separado. El procesamiento puede tardar un breve
período después del impacto.

La información faltante puede limitar la detección. Informa al administrador
si un contacto no se cuenta o aparece un falso positivo, indicando la sesión
y lo ocurrido.

## Severidad
Considera intensidad del impacto, velocidad relativa, pérdida de velocidad
asociada a la colisión y si algún auto involucrado entra en trompo. Que otro
auto reduzca velocidad no reemplaza la necesidad de contacto. Un trompo sin
contacto no crea por sí solo un incidente de contacto.

| Categoría | Significado | Puntos por defecto |
| --- | --- | --- |
| Mínimo | Contacto de poca entidad | 0 |
| Leve/normal | Contacto por encima del mínimo | 1 |
| Heavy/fuerte | Impacto mayor o pérdida importante de velocidad asociada | 2 |
| Contacto con spin | Contacto con un trompo asociado | 3 |

## Puntos y sanciones
El administrador puede elegir entre 0 y 10 puntos para contactos leves, heavy
y spin. Cambiar puntos no modifica cómo se determina la severidad.
Un contacto de cero puntos puede quedar registrado.

Con los controles de servidor activos, los incidentes nuevos usan la puntuación
configurada en el servidor. No se recalculan puntos ni sanciones anteriores.
Mantén esos controles activos para una puntuación uniforme en la liga.

Los puntos alimentan la escala de sanciones. Los cortes tienen un contador
separado. Consulta [sanciones](rules-and-sanctions.md) y [ajustes](server-admin.md).

