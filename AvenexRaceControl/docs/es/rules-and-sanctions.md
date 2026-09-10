# Reglas y sanciones

## Advertencia
Avisa de un umbral de puntos de incidente. No añade tiempo ni exige entrar en
boxes. Cada nivel activo de la escala se emite una vez por estado de carrera.
Si un incidente cruza varios umbrales, se elige el nivel más alto aplicable,
no todas las sanciones intermedias.

## Penalización de tiempo
Añade los segundos configurados al resultado final. No requiere detenerse.
Un umbral de 2 puntos con sanción de 3 segundos significa +3 s, no +6 s.
Los incumplimientos de acelerador por cortes pueden añadir más segundos.

El monitor muestra el total: +3 s y dos sanciones de +5 s producen +13 s.
Cambiar ajustes no modifica sanciones emitidas. Cumplir DT o Stop & Go no
elimina los segundos acumulados.

El administrador debe activar el procesamiento post-carrera para aplicar el
tiempo a los resultados. El archivo `cfg/avenex_post_race_results.html` muestra
tiempo original, recargo y resultado ajustado. Compara tiempos totales con
igual cantidad de vueltas, no tiempos de una vuelta aislada. El último reporte
reemplaza al anterior; archívalo si necesitas conservarlo.

El reporte se genera al finalizar resultados, cuando terminan los participantes
pertinentes o vence la espera de fin de carrera. Cruzar primero la meta no
significa necesariamente que el reporte ya esté disponible.

## Drive-through
Cumple la obligación en boxes antes del plazo de vueltas indicado. Esta edición
reconoce el servicio mientras el auto está en pit lane dentro del límite de
velocidad más tolerancia; no verifica todo el trayecto de entrada a salida.
No cumplir a tiempo escala a descalificación.

## Stop & Go
Detén el auto en boxes durante el tiempo de Avenex enforcement. Si superas la
velocidad considerada detenido antes de completar la espera, el contador
reinicia. Completar la espera sirve la sanción; vencer el plazo de vueltas
sin cumplirla escala a descalificación. Avenex no teletransporta el auto ni
bloquea su acelerador.

## Descalificación
Es una sanción terminal. Según la configuración, aplica descalificación nativa
o expulsa al piloto del servidor. No puede cumplirse para seguir en carrera.

## Cortes de pista
Salir con las cuatro ruedas suma inmediatamente un corte. Permanecer fuera
no repite el contador; volver y salir otra vez puede sumar otro.
Levantar el acelerador no borra el corte.

Después del margen de reacción configurable, mantén el acelerador dentro
del máximo durante el período de control. El primer exceso en ese período
añade inmediatamente el tiempo configurado, una vez por corte. Volver a pista
no cancela esa obligación.

Al llegar al límite se emite DT, Stop & Go o DSQ según la configuración.
El contador se congela y se cancelan los controles de acelerador pendientes:
otras salidas no suman cortes ni tiempo mientras esa sanción está pendiente.
Cumplir su DT/Stop & Go reinicia solo cortes a cero, no los segundos acumulados.
Los cortes posteriores pueden volver a añadir tiempo.

## Plazos y sanciones simultáneas
Los plazos incluyen la vuelta actual: no esperes al siguiente cruce para comenzar
a cumplir. La app mantiene una obligación DT/Stop & Go pendiente, no una cola
de sanciones idénticas. Los nuevos ajustes afectan obligaciones futuras.

## Otros controles
VSC/FCY es una neutralización con velocidad limitada, no un safety car físico.
La activación manual y automática son opciones separadas. Respeta la velocidad
y la cuenta indicadas cuando el servidor lo active.

Las tarjetas deshabilitadas de bandera azul, amarilla o exceso en boxes son
controles no disponibles; no dependas de ellas para aplicar reglas de liga.
La visibilidad de overlays es independiente del cumplimiento de sanciones.

Consulta [Administración](server-admin.md) y [puntos de incidente](incidents.md).

