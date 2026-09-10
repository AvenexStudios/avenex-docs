# Referencia del admin

Actualizado: 2026-09-10. Catalogo de las 63 opciones del esquema del admin.
Los defaults de fabrica no sustituyen los valores guardados de cada servidor.

## Guardar, activar y restablecer

Guardar aplica y persiste la configuracion; los clientes conectados reciben los valores.
Recargar permite comprobar lo guardado. Exportar/importar mueve configuracion, no
resultados ni sanciones cumplidas. No publique tokens ni archivos privados exportados.

El control de cada campo no siempre significa "desactivar esa regla":
en un interruptor, desmarcarlo fuerza false; en los umbrales de la escala,
desmarcarlo deshabilita esa sancion. En otros selectores desmarcarlo permite
el valor local del cliente: NO equivale a poner el numero en cero.
Para carreras oficiales mantenga activos los controles de servidor de puntuacion.

Reset de un campo recupera su default; no limpia la carrera.
El reset de estado de carrera borra puntos y memoria de sanciones de la sesion;
es una operacion distinta. Una nueva sesion tambien reinicia el estado del cliente.
Modificar configuracion no recalcula sanciones ni puntos anteriores.

## Como configurar

- Puntuacion: en Penalty ladder elija puntos por contacto leve, heavy y spin.
  Defaults 1, 2 y 3; rango 0..10. Contacto minimo conserva su default de 0.
  Un 0 asigna cero puntos, no cambia la deteccion ni la severidad.
- Escala: habilite la escala y solo los umbrales que quiera probar. Si varios
  se cruzan de golpe se selecciona el nivel mas alto alcanzado, no una cola
  de todas las sanciones intermedias.
- Cortes: habilite la regla, elija limite y DT/S&G/DSQ, margen, acelerador maximo,
  duracion y tiempo por exceso. Ejemplo: margen 1 s, maximo 20%, control 3 s y
  +5 s. Antes de terminar el margen no hay sancion de acelerador; durante los
  siguientes 3 s el primer exceso suma 5 s inmediatamente.
- Servicio: use Avenex enforcement para vueltas de plazo, velocidad de boxes
  y detencion S&G. No use los selectores de bloqueo nativo para configurar
  el Stop & Go propio.
- Tiempo: habilite Post-race penalties para aplicar el total emitido a los
  resultados finales y HTML. Seconds per penalty configura el tiempo de la
  escala de incidentes; los cortes tienen su propio selector de segundos.
- VSC: el limite de velocidad, margen y tolerancia son independientes de la
  regla de acelerador de cortes. La activacion manual y automatica son opciones
  diferentes. Estos modulos no quedan aprobados por la aprobacion de cortes.

Consulte [sanciones](rules-and-sanctions.md) e [incidentes](incidents.md).

## Estado funcional

| Modulo | Situacion al 2026-09-10 |
| --- | --- |
| Cortes | Etapa funcional aprobada por el propietario; arte final UX pendiente |
| DT, S&G y DSQ | Pruebas individuales y combinadas reportadas como satisfactorias; confirmar valores configurables en cada despliegue |
| Tiempo y resultados | Resultados nativos y HTML aceptados por el propietario; mantener revision de la generacion de informes |
| Selectores de puntos | Implementados y con tests; pendientes de nueva prueba in-game |
| Deteccion de incidentes | En validacion; no implica atribucion de culpa |
| VSC manual/automatico | Disponible para pruebas, sin aprobacion general registrada |
| Banderas azules, amarillas, exceso en boxes, HUD feedback | Tarjetas marcadas no implementadas en el admin; no asumir validacion productiva |

## Opciones por tarjeta

"Implementada" describe la disponibilidad del esquema, no una aprobacion de QA.
Las descripciones de controles nativos legados se conservan como referencia:
el flujo de sanciones actual solo invoca enforcement nativo para DSQ.

### Escala de sanciones (Penalty ladder)

Disponibilidad en admin: implementada.

#### Puntos por contacto leve

Puntos por contacto normal o leve. Los contactos minimos siguen en cero; los cambios afectan solo incidentes nuevos.

- Clave: `CONTACT_POINTS`.
- Default: `1` puntos.
- Opciones: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`.

#### Puntos por heavy

Puntos por contacto fuerte; no cambia la deteccion de severidad.

- Clave: `HEAVY_CONTACT_POINTS`.
- Default: `2` puntos.
- Opciones: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`.

#### Puntos por spin

Puntos por contacto con trompo detectado; un trompo sin contacto no es un incidente.

- Clave: `SPIN_CONTACT_POINTS`.
- Default: `3` puntos.
- Opciones: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`.

#### Escala de incidentes

Aplica sanciones oficiales segun los puntos de incidente acumulados.

- Clave: `PENALTIES_ENABLED`.
- Default: `false`.
- Opciones: `true`, `false`.

#### Advertencia en

Puntos de incidente necesarios antes de emitir una advertencia.

- Clave: `WARNING_AT`.
- Default: `8` puntos.
- Opciones: `2`, `4`, `6`, `8`, `10`, `12`, `16`.

#### Tiempo extra en

Puntos de incidente necesarios antes de sumar tiempo post-carrera.

- Clave: `TIME_PENALTY_AT`.
- Default: `12` puntos.
- Opciones: `2`, `4`, `6`, `8`, `10`, `12`, `16`, `24`.

#### Drive-through en

Puntos de incidente necesarios antes de emitir un drive-through.

- Clave: `DRIVE_THROUGH_AT`.
- Default: `16` puntos.
- Opciones: `2`, `4`, `6`, `8`, `10`, `12`, `16`, `20`, `24`.

#### Stop and go en

Puntos de incidente necesarios antes de emitir un stop and go.

- Clave: `STOP_AND_GO_AT`.
- Default: `20` puntos.
- Opciones: `2`, `4`, `6`, `8`, `10`, `12`, `16`, `20`, `24`, `30`.

#### Descalificar en

Puntos de incidente necesarios antes de descalificar.

- Clave: `DISQUALIFY_AT`.
- Default: `30` puntos.
- Opciones: `2`, `4`, `6`, `8`, `10`, `16`, `20`, `24`, `30`, `40`, `60`.

### Cortes de pista (Track cuts)

Disponibilidad en admin: implementada.

#### Regla de cortes

Cuenta cortes de pista de forma independiente de los puntos de incidente.

- Clave: `CUTS_ENABLED`.
- Default: `false`.
- Opciones: `true`, `false`.

#### Limite de cortes

Cuenta salidas con 4 ruedas hasta este limite. Pausa cortes y sanciones de acelerador hasta servir la sancion.

- Clave: `CUTS_LIMIT`.
- Default: `3` cortes.
- Opciones: `1`, `2`, `3`, `4`, `5`, `6`, `8`, `10`.

#### Margen de reaccion

Tiempo desde la salida de pista para soltar el acelerador. El control comienza al terminar este margen; el corte se cuenta igualmente.

- Clave: `CUT_GRACE_MS`.
- Default: `1000` ms.
- Opciones: `0`, `500`, `1000`, `1500`, `2000`, `3000`, `5000`.

#### Acelerador maximo

Porcentaje maximo durante el periodo de control, despues del margen de reaccion.

- Clave: `CUT_MAX_THROTTLE_PERCENT`.
- Default: `10` %.
- Opciones: `0`, `10`, `20`, `30`, `40`, `50`, `60`, `70`, `80`, `90`, `100`.

#### Duracion del control

Mantener el acelerador dentro del maximo durante todo este periodo tras el margen, incluso al volver a pista.

- Clave: `CUT_THROTTLE_HOLD_SECONDS`.
- Default: `3` s.
- Opciones: `1`, `2`, `3`, `4`, `5`, `10`, `15`.

#### Tiempo por incumplimiento

Tras el margen de reaccion, suma estos segundos inmediatamente al primer exceso, una vez por corte. El control se suspende al alcanzar el limite de cortes.

- Clave: `CUT_TIME_PENALTY_SECONDS`.
- Default: `5` s.
- Opciones: `1`, `2`, `3`, `5`, `10`, `15`, `20`, `30`, `60`.

#### Sancion por cortes

Sancion oficial enviada cuando se alcanza el limite de cortes.

- Clave: `CUTS_PENALTY_ACTION`.
- Default: `DRIVE_THROUGH`.
- Opciones: `DRIVE_THROUGH`, `STOP_AND_GO`, `DISQUALIFICATION`.

### Banderas azules (Blue flags)

Disponibilidad en admin: no implementada / deshabilitada.

#### Regla de bandera azul

Exige dejar pasar al auto rapido especifico que viene atras.

- Clave: `BLUE_FLAGS_ENABLED`.
- Default: `false`.
- Opciones: `true`, `false`.

#### Ventana para ceder

Segundos antes de penalizar una bandera azul ignorada.

- Clave: `BLUE_FLAG_YIELD_SECONDS`.
- Default: `10` s.
- Opciones: `5`, `10`, `15`, `20`.

#### Distancia atras

Distancia normalizada de pista usada para elegir el objetivo de atras.

- Clave: `BLUE_FLAG_MAX_BEHIND_SPLINE_DELTA`.
- Default: `0.18` pista.
- Opciones: `0.08`, `0.12`, `0.18`, `0.25`.

#### Sancion de bandera azul

Sancion oficial enviada si no se deja pasar al objetivo.

- Clave: `BLUE_FLAG_PENALTY_ACTION`.
- Default: `DRIVE_THROUGH`.
- Opciones: `DRIVE_THROUGH`, `STOP_AND_GO`, `DISQUALIFICATION`.

### Banderas amarillas (Yellow flags)

Disponibilidad en admin: no implementada / deshabilitada.

#### Regla de bandera amarilla

Exige bajar velocidad mientras una bandera amarilla esta activa.

- Clave: `YELLOW_FLAGS_ENABLED`.
- Default: `false`.
- Opciones: `true`, `false`.

#### Ventana para bajar

Tiempo disponible para bajar velocidad bajo amarilla.

- Clave: `YELLOW_FLAG_GRACE_MS`.
- Default: `3000` ms.
- Opciones: `1000`, `2000`, `3000`, `5000`.

#### Reduccion requerida

Reduccion de velocidad necesaria bajo amarilla.

- Clave: `YELLOW_FLAG_SPEED_DROP_KMH`.
- Default: `10` km/h.
- Opciones: `5`, `10`, `15`, `20`.

#### Sancion de amarilla

Sancion oficial enviada si el piloto no baja velocidad.

- Clave: `YELLOW_FLAG_PENALTY_ACTION`.
- Default: `DRIVE_THROUGH`.
- Opciones: `DRIVE_THROUGH`, `STOP_AND_GO`, `DISQUALIFICATION`.

### Virtual safety car (Virtual safety car)

Disponibilidad en admin: implementada.

#### Regla VSC / FCY

Activa el virtual safety car / full-course-yellow de Avenex y su control de velocidad.

- Clave: `VSC_ENABLED`.
- Default: `false`.
- Opciones: `true`, `false`.

#### VSC manual activo

Activa o limpia el VSC desde el panel admin del servidor.

- Clave: `VSC_MANUAL_ACTIVE`.
- Default: `false`.
- Opciones: `true`, `false`.

#### Limite VSC

Velocidad maxima mientras el VSC esta activo.

- Clave: `VSC_SPEED_LIMIT_KMH`.
- Default: `80` km/h.
- Opciones: `40`, `50`, `60`, `80`, `100`.

#### Cuenta para bajar

Segundos disponibles para bajar velocidad cuando se activa el VSC.

- Clave: `VSC_SLOWDOWN_GRACE_SECONDS`.
- Default: `10` s.
- Opciones: `5`, `8`, `10`, `15`, `20`.

#### Tolerancia velocidad

Km/h extra permitidos sobre el limite VSC.

- Clave: `VSC_SPEED_TOLERANCE_KMH`.
- Default: `3` km/h.
- Opciones: `0`, `2`, `3`, `5`, `10`.

#### Debounce exceso

Tiempo sobre el limite VSC antes de emitir sancion.

- Clave: `VSC_SPEEDING_DEBOUNCE_MS`.
- Default: `500` ms.
- Opciones: `250`, `500`, `1000`, `2000`.

#### Sancion exceso VSC

Sancion enviada si un piloto supera el limite VSC despues de la cuenta.

- Clave: `VSC_PENALTY_ACTION`.
- Default: `DRIVE_THROUGH`.
- Opciones: `DRIVE_THROUGH`, `STOP_AND_GO`, `DISQUALIFICATION`.

#### Auto-activar

Activa VSC automaticamente por incidentes fuertes, multiples autos o autos detenidos.

- Clave: `VSC_AUTO_DEPLOY_ENABLED`.
- Default: `false`.
- Opciones: `true`, `false`.

#### Contactos cluster

Cantidad de contactos cercanos necesaria para auto-activar VSC.

- Clave: `VSC_AUTO_MIN_CONTACTS`.
- Default: `2` contactos.
- Opciones: `2`, `3`, `4`.

#### Ventana cluster

Ventana temporal para agrupar incidentes multiples.

- Clave: `VSC_AUTO_CLUSTER_WINDOW_MS`.
- Default: `3000` ms.
- Opciones: `1500`, `2500`, `3000`, `5000`.

#### Distancia cluster

Distancia maxima entre contactos del mismo cluster VSC.

- Clave: `VSC_AUTO_CLUSTER_DISTANCE_METERS`.
- Default: `50` m.
- Opciones: `25`, `50`, `75`, `100`.

#### Impacto fuerte

Velocidad de impacto que activa VSC inmediatamente.

- Clave: `VSC_AUTO_HEAVY_CONTACT_KMH`.
- Default: `35` km/h.
- Opciones: `25`, `35`, `45`, `60`.

#### Velocidad detenido

Velocidad considerada detenido para un auto post-contacto en pista.

- Clave: `VSC_AUTO_STOPPED_SPEED_KMH`.
- Default: `5` km/h.
- Opciones: `2`, `5`, `8`, `10`.

#### Tiempo detenido

Tiempo que un auto contactado debe quedar detenido en pista antes de activar VSC.

- Clave: `VSC_AUTO_STOPPED_DURATION_MS`.
- Default: `5000` ms.
- Opciones: `3000`, `5000`, `8000`, `10000`.

#### Ventana post-contacto

Antiguedad maxima del contacto para considerar peligroso un auto detenido.

- Clave: `VSC_AUTO_STOPPED_CONTACT_WINDOW_MS`.
- Default: `15000` ms.
- Opciones: `10000`, `15000`, `20000`, `30000`.

#### Demora auto-clear

Segundos sin peligro nuevo antes de limpiar el VSC automatico.

- Clave: `VSC_AUTO_CLEAR_SECONDS`.
- Default: `20` s.
- Opciones: `10`, `20`, `30`, `45`, `60`.

### Exceso en boxes (Pit speeding)

Disponibilidad en admin: no implementada / deshabilitada.

#### Regla de velocidad en boxes

Detecta exceso de velocidad en boxes desde la telemetria del cliente.

- Clave: `PIT_SPEEDING_ENABLED`.
- Default: `false`.
- Opciones: `true`, `false`.

#### Tolerancia

Velocidad permitida sobre el limite de boxes antes de sancionar.

- Clave: `PIT_SPEEDING_TOLERANCE_KMH`.
- Default: `2` km/h.
- Opciones: `0`, `2`, `5`, `10`.

#### Debounce

Tiempo sobre el limite antes de emitir una sancion.

- Clave: `PIT_SPEEDING_DEBOUNCE_MS`.
- Default: `250` ms.
- Opciones: `100`, `250`, `500`, `1000`.

#### Sancion por boxes

Sancion oficial enviada por exceso de velocidad en boxes.

- Clave: `PIT_SPEEDING_PENALTY_ACTION`.
- Default: `DRIVE_THROUGH`.
- Opciones: `DRIVE_THROUGH`, `STOP_AND_GO`, `DISQUALIFICATION`.

### Enforcement Avenex (Avenex enforcement)

Disponibilidad en admin: implementada.

#### Servicio DT/S&G Avenex

Controla drive-through y stop-and-go desde Avenex en lugar del HUD nativo AC/CSP.

- Clave: `RACE_PENALTY_SERVICE_ENABLED`.
- Default: `true`.
- Opciones: `true`, `false`.

#### Limite DT

Limite basado en la vuelta actual antes de escalar un DT incumplido a descalificacion.

- Clave: `DRIVE_THROUGH_DEADLINE_LAPS`.
- Default: `1` vueltas.
- Opciones: `1`, `2`, `3`.

#### Tolerancia DT

Km/h extra permitidos sobre el limite de boxes al cumplir un drive-through.

- Clave: `DRIVE_THROUGH_PIT_SPEED_TOLERANCE_KMH`.
- Default: `2` km/h.
- Opciones: `0`, `2`, `5`, `10`.

#### Limite pit fallback

Limite de velocidad fallback si el cliente no puede leer el valor de sesion.

- Clave: `RACE_PENALTY_PIT_SPEED_LIMIT_KMH`.
- Default: `80` km/h.
- Opciones: `30`, `50`, `60`, `80`.

#### Limite S&G

Limite basado en la vuelta actual antes de escalar un stop and go incumplido a descalificacion.

- Clave: `STOP_AND_GO_DEADLINE_LAPS`.
- Default: `1` vueltas.
- Opciones: `1`, `2`, `3`.

#### Detencion S&G

Segundos que el piloto debe quedar detenido en boxes.

- Clave: `STOP_AND_GO_SECONDS`.
- Default: `5` s.
- Opciones: `3`, `5`, `10`, `15`, `30`.

#### Velocidad detenido

Velocidad maxima considerada detenido para contar el stop and go.

- Clave: `STOP_AND_GO_STOP_SPEED_KMH`.
- Default: `1` km/h.
- Opciones: `0`, `1`, `2`, `5`.

### Tiempo post-carrera (Post-race time)

Disponibilidad en admin: implementada.

#### Penalizaciones post-carrera

Suma los segundos sancionados a los resultados finales nativos y al reporte de auditoria.

- Clave: `POST_RACE_TIME_PENALTIES_ENABLED`.
- Default: `false`.
- Opciones: `true`, `false`.

#### Segundos por sancion

Segundos asignados al alcanzar el umbral de penalizacion de tiempo.

- Clave: `TIME_PENALTY_SECONDS_PER_POINT`.
- Default: `1` s.
- Opciones: `0`, `1`, `2`, `3`, `5`, `10`.

### Enforcement nativo (Native enforcement)

Disponibilidad en admin: implementada.

#### Enforcement nativo

Usa el HUD nativo de CSP para drive-through, bloqueo y bandera negra como canal Native Enforcement HUD.

- Clave: `NATIVE_ENFORCEMENT_ENABLED`.
- Default: `false`.
- Opciones: `true`, `false`.

Control nativo legado: no cambia la duracion ni el servicio del DT/S&G propio.

#### Limite DT

Parametro CSP de vencimiento de drive-through basado en la vuelta actual.

- Clave: `NATIVE_DRIVE_THROUGH_LAPS`.
- Default: `2` vueltas.
- Opciones: `1`, `2`, `3`.

Control nativo legado: no cambia la duracion ni el servicio del DT/S&G propio.

#### Duracion de bloqueo

Segundos con controles bloqueados para stop and go.

- Clave: `NATIVE_STOP_AND_GO_SECONDS`.
- Default: `5` s.
- Opciones: `5`, `10`, `15`, `30`.

Control nativo legado: no cambia la duracion ni el servicio del DT/S&G propio.

#### Mensajes de chat del servidor

Envia mensajes de sancion Avenex ademas del HUD nativo.

- Clave: `SEND_PENALTY_CHAT_MESSAGES`.
- Default: `true`.
- Opciones: `true`, `false`.

### Overlays del servidor (Server overlays)

Disponibilidad en admin: implementada.

#### Overlays Avenex

Fuerza el encendido o apagado de los canales de overlay Avenex en los clientes conectados. Este valor del servidor pisa el INI local del cliente.

- Clave: `UI_OVERLAY_ENABLED`.
- Default: `true`.
- Opciones: `true`, `false`.

### Feedback HUD (HUD feedback)

Disponibilidad en admin: no implementada / deshabilitada.

#### Monitor de incidentes

Muestra el monitor compacto de incidentes.

- Clave: `UI_SHOW_MAIN`.
- Default: `true`.
- Opciones: `true`, `false`.

#### Monitor de cortes

Muestra el monitor compacto de cortes.

- Clave: `UI_SHOW_CUTS`.
- Default: `true`.
- Opciones: `true`, `false`.

#### Banners de Race Control

Muestra overlays del canal Race Control Banner de Avenex.

- Clave: `UI_SHOW_TOASTS`.
- Default: `true`.
- Opciones: `true`, `false`.

#### Advisories de cumplimiento

Muestra overlays del canal Compliance Advisory de Avenex.

- Clave: `UI_SHOW_FLAGS`.
- Default: `true`.
- Opciones: `true`, `false`.

#### Monitor post-carrera

Muestra el monitor compacto de segundos post-carrera.

- Clave: `UI_PENALTY_SECONDS_MONITOR_ENABLED`.
- Default: `false`.
- Opciones: `true`, `false`.

