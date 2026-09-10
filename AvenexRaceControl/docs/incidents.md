# Incidentes y severidad

Avenex cuenta participacion en accidentes; no decide quien tuvo la culpa.

## Que hace que se cuente un incidente

Debe existir evidencia de contacto entre autos y participacion del piloto.
Pasar muy cerca, que otro auto frene o un cambio de velocidad por si solo no
deben contar como choque. En el modo online actual se utilizan eventos de
contacto del servidor; la telemetria ayuda a evaluar sus consecuencias.
El modo offline utiliza las fuentes de contacto del cliente y requiere su
propia validacion. Los contactos con el entorno no forman parte de la ruta
actual de eventos online entre autos.

Una colision puede generar varias observaciones. Avenex agrupa observaciones
cercanas que pertenecen al mismo accidente para no cobrar cada muestra como
un choque nuevo. Por eso el numero de toques visibles no siempre coincide
con el numero de incidentes. Hay un periodo de observacion: el contador no
necesariamente cambia en el instante exacto del impacto.

Sin evidencia suficiente no debe inventarse un contacto. Latencia, telemetria
faltante y autos de IA que desaparecen pueden limitar el analisis. Si un
choque real no suma o una pasada cercana suma, conserve hora y contexto para
revisar los registros; no habilite grabacion intensiva permanentemente.

## Como se determina la severidad

Se considera la intensidad del contacto, la velocidad relativa en el impacto
y la perdida de velocidad asociada al accidente. Tambien se observa si un auto
implicado entra en trompo, a partir de su movimiento y cambio de orientacion.
La velocidad del rival ayuda a entender el impacto, pero nunca sustituye
la necesidad de contacto.

| Clasificacion | Significado funcional | Puntos por defecto |
| --- | --- | --- |
| Minimo (MINOR_CONTACT) | Contacto de poca entidad | 0 |
| Leve/normal (CONTACT) | Contacto que supera el nivel minimo | 1 |
| Fuerte (HEAVY_CONTACT) | Impacto de mayor intensidad o perdida importante de velocidad | 2 |
| Contacto con trompo (CONTACT_SPIN) | Contacto con evidencia de spin asociada al accidente | 3 |

Un trompo sin contacto no crea por si solo un incidente de contacto.
La clasificacion describe el accidente, no culpabilidad ni intencion.
No presupone que el auto del piloto sea siempre el unico afectado.

## Puntuacion configurable

En Penalty ladder se pueden elegir de 0 a 10 puntos para leve, heavy y spin.
Los defaults son 1, 2 y 3; el minimo conserva 0 por defecto.
Cambiar puntos no cambia los criterios que distinguen severidades.
Un evento de cero puntos puede seguir siendo un evento registrado.

Con los controles de servidor activos, la autoridad aplica el valor configurado
segun la clasificacion del nuevo incidente, incluso si el cliente aun envia
una puntuacion anterior. Los valores se comunican al cliente. Al editar una
puntuacion no se recalculan incidentes anteriores ni sanciones ya emitidas.
Si se desmarca el control de un selector, se permite la puntuacion local:
mantenga esos controles activos para una regla uniforme entre pilotos.

Los puntos alimentan la escala de sanciones; los cortes de pista y sus
recargos por acelerador tienen reglas independientes.

Consulte [reglas y sanciones](rules-and-sanctions.md) y [admin](server-admin.md).

