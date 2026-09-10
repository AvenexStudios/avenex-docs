# Administración del servidor

Configura las reglas en `/avenex/admin` de la dirección HTTP del servidor.
Mantén privadas las credenciales.

## Guardar y activar reglas
Guardar aplica y conserva las selecciones. Recarga para comprobar lo guardado.
Importar/exportar transfiere ajustes, no sanciones cumplidas ni resultados.
Respalda la configuración antes de importar.

El control de servidor de cada campo tiene distintos efectos:
- En un interruptor, desactivarlo fuerza ese ajuste a apagado.
- En un umbral de la escala, desactivarlo deshabilita esa sanción.
- En otros selectores numéricos, desactivarlo permite el valor local del
  cliente. No equivale a cero. Mantén activos los controles de puntuación para
  usar reglas uniformes.

Reset de un campo restaura su valor predeterminado. El reinicio de estado de
carrera es distinto: borra puntos y memoria de sanciones de sesión.
Los cambios no recalculan puntos ni sanciones anteriores. El margen y la
duración de un corte se toman cuando comienza ese corte.

## Elegir una configuración
Primero elige puntos por contacto (defaults 1/2/3) y después los niveles y
umbrales de la escala. Configura el servicio en Avenex enforcement, no en
controles nativos heredados. Activa el procesamiento post-carrera para aplicar
los segundos acumulados a los resultados.

Para cortes elige límite, sanción, margen de reacción, máximo de acelerador,
duración del control y tiempo por incumplimiento. Ejemplo: margen 1 s,
acelerador 20%, control 3 s y +5 s. El exceso durante el margen está permitido;
el primer exceso durante el control suma +5 s inmediatamente.

VSC/FCY tiene su propio límite de velocidad y cuenta para reducirla, separados
de la regla de acelerador de cortes. No dependas de tarjetas deshabilitadas.

Consulta [sanciones](rules-and-sanctions.md), [puntuación](incidents.md) y
[versiones](versions.md).

## Ajustes
Los valores siguientes son de fábrica, no necesariamente los guardados.

### Escala de sanciones


#### Puntos por contacto leve

Puntos por contacto normal o leve. Los contactos minimos siguen en cero; los cambios afectan solo incidentes nuevos.

- Valor predeterminado: **1** puntos.
- Opciones: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

#### Puntos por heavy

Puntos por contacto fuerte; no cambia la deteccion de severidad.

- Valor predeterminado: **2** puntos.
- Opciones: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

#### Puntos por spin

Puntos por contacto con trompo detectado; un trompo sin contacto no es un incidente.

- Valor predeterminado: **3** puntos.
- Opciones: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

#### Escala de incidentes

Aplica sanciones oficiales segun los puntos de incidente acumulados.

- Valor predeterminado: **false**.
- Opciones: Activado, Desactivado.

#### Advertencia en

Puntos de incidente necesarios antes de emitir una advertencia.

- Valor predeterminado: **8** puntos.
- Opciones: 2, 4, 6, 8, 10, 12, 16.

#### Tiempo extra en

Puntos de incidente necesarios antes de sumar tiempo post-carrera.

- Valor predeterminado: **12** puntos.
- Opciones: 2, 4, 6, 8, 10, 12, 16, 24.

#### Drive-through en

Puntos de incidente necesarios antes de emitir un drive-through.

- Valor predeterminado: **16** puntos.
- Opciones: 2, 4, 6, 8, 10, 12, 16, 20, 24.

#### Stop and go en

Puntos de incidente necesarios antes de emitir un stop and go.

- Valor predeterminado: **20** puntos.
- Opciones: 2, 4, 6, 8, 10, 12, 16, 20, 24, 30.

#### Descalificar en

Puntos de incidente necesarios antes de descalificar.

- Valor predeterminado: **30** puntos.
- Opciones: 2, 4, 6, 8, 10, 16, 20, 24, 30, 40, 60.

### Cortes de pista


#### Regla de cortes

Cuenta cortes de pista de forma independiente de los puntos de incidente.

- Valor predeterminado: **false**.
- Opciones: Activado, Desactivado.

#### Limite de cortes

Cuenta salidas con 4 ruedas hasta este limite. Pausa cortes y sanciones de acelerador hasta servir la sancion.

- Valor predeterminado: **3** cortes.
- Opciones: 1, 2, 3, 4, 5, 6, 8, 10.

#### Margen de reaccion

Tiempo desde la salida de pista para soltar el acelerador. El control comienza al terminar este margen; el corte se cuenta igualmente.

- Valor predeterminado: **1000** ms.
- Opciones: 0, 500, 1000, 1500, 2000, 3000, 5000.

#### Acelerador maximo

Porcentaje maximo durante el periodo de control, despues del margen de reaccion.

- Valor predeterminado: **10** %.
- Opciones: 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100.

#### Duracion del control

Mantener el acelerador dentro del maximo durante todo este periodo tras el margen, incluso al volver a pista.

- Valor predeterminado: **3** s.
- Opciones: 1, 2, 3, 4, 5, 10, 15.

#### Tiempo por incumplimiento

Tras el margen de reaccion, suma estos segundos inmediatamente al primer exceso, una vez por corte. El control se suspende al alcanzar el limite de cortes.

- Valor predeterminado: **5** s.
- Opciones: 1, 2, 3, 5, 10, 15, 20, 30, 60.

#### Sancion por cortes

Sancion oficial enviada cuando se alcanza el limite de cortes.

- Valor predeterminado: **DRIVE_THROUGH**.
- Opciones: Drive-through, Stop and go, Descalificacion.

### Banderas azules

Esta tarjeta no está disponible para configurar reglas en esta edición.

#### Regla de bandera azul

Exige dejar pasar al auto rapido especifico que viene atras.

- Valor predeterminado: **false**.
- Opciones: Activado, Desactivado.

#### Ventana para ceder

Segundos antes de penalizar una bandera azul ignorada.

- Valor predeterminado: **10** s.
- Opciones: 5, 10, 15, 20.

#### Distancia atras

Distancia normalizada de pista usada para elegir el objetivo de atras.

- Valor predeterminado: **0.18** pista.
- Opciones: 0.08, 0.12, 0.18, 0.25.

#### Sancion de bandera azul

Sancion oficial enviada si no se deja pasar al objetivo.

- Valor predeterminado: **DRIVE_THROUGH**.
- Opciones: Drive-through, Stop and go, Descalificacion.

### Banderas amarillas

Esta tarjeta no está disponible para configurar reglas en esta edición.

#### Regla de bandera amarilla

Exige bajar velocidad mientras una bandera amarilla esta activa.

- Valor predeterminado: **false**.
- Opciones: Activado, Desactivado.

#### Ventana para bajar

Tiempo disponible para bajar velocidad bajo amarilla.

- Valor predeterminado: **3000** ms.
- Opciones: 1000, 2000, 3000, 5000.

#### Reduccion requerida

Reduccion de velocidad necesaria bajo amarilla.

- Valor predeterminado: **10** km/h.
- Opciones: 5, 10, 15, 20.

#### Sancion de amarilla

Sancion oficial enviada si el piloto no baja velocidad.

- Valor predeterminado: **DRIVE_THROUGH**.
- Opciones: Drive-through, Stop and go, Descalificacion.

### Virtual safety car


#### Regla VSC / FCY

Activa el virtual safety car / full-course-yellow de Avenex y su control de velocidad.

- Valor predeterminado: **false**.
- Opciones: Activado, Desactivado.

#### VSC manual activo

Activa o limpia el VSC desde el panel admin del servidor.

- Valor predeterminado: **false**.
- Opciones: Activado, Desactivado.

#### Limite VSC

Velocidad maxima mientras el VSC esta activo.

- Valor predeterminado: **80** km/h.
- Opciones: 40, 50, 60, 80, 100.

#### Cuenta para bajar

Segundos disponibles para bajar velocidad cuando se activa el VSC.

- Valor predeterminado: **10** s.
- Opciones: 5, 8, 10, 15, 20.

#### Tolerancia velocidad

Km/h extra permitidos sobre el limite VSC.

- Valor predeterminado: **3** km/h.
- Opciones: 0, 2, 3, 5, 10.

#### Debounce exceso

Tiempo sobre el limite VSC antes de emitir sancion.

- Valor predeterminado: **500** ms.
- Opciones: 250, 500, 1000, 2000.

#### Sancion exceso VSC

Sancion enviada si un piloto supera el limite VSC despues de la cuenta.

- Valor predeterminado: **DRIVE_THROUGH**.
- Opciones: Drive-through, Stop and go, Descalificacion.

#### Auto-activar

Activa VSC automaticamente por incidentes fuertes, multiples autos o autos detenidos.

- Valor predeterminado: **false**.
- Opciones: Activado, Desactivado.

#### Contactos cluster

Cantidad de contactos cercanos necesaria para auto-activar VSC.

- Valor predeterminado: **2** contactos.
- Opciones: 2, 3, 4.

#### Ventana cluster

Ventana temporal para agrupar incidentes multiples.

- Valor predeterminado: **3000** ms.
- Opciones: 1500, 2500, 3000, 5000.

#### Distancia cluster

Distancia maxima entre contactos del mismo cluster VSC.

- Valor predeterminado: **50** m.
- Opciones: 25, 50, 75, 100.

#### Impacto fuerte

Velocidad de impacto que activa VSC inmediatamente.

- Valor predeterminado: **35** km/h.
- Opciones: 25, 35, 45, 60.

#### Velocidad detenido

Velocidad considerada detenido para un auto post-contacto en pista.

- Valor predeterminado: **5** km/h.
- Opciones: 2, 5, 8, 10.

#### Tiempo detenido

Tiempo que un auto contactado debe quedar detenido en pista antes de activar VSC.

- Valor predeterminado: **5000** ms.
- Opciones: 3000, 5000, 8000, 10000.

#### Ventana post-contacto

Antiguedad maxima del contacto para considerar peligroso un auto detenido.

- Valor predeterminado: **15000** ms.
- Opciones: 10000, 15000, 20000, 30000.

#### Demora auto-clear

Segundos sin peligro nuevo antes de limpiar el VSC automatico.

- Valor predeterminado: **20** s.
- Opciones: 10, 20, 30, 45, 60.

### Exceso en boxes

Esta tarjeta no está disponible para configurar reglas en esta edición.

#### Regla de velocidad en boxes

Detecta exceso de velocidad en boxes desde la telemetria del cliente.

- Valor predeterminado: **false**.
- Opciones: Activado, Desactivado.

#### Tolerancia

Velocidad permitida sobre el limite de boxes antes de sancionar.

- Valor predeterminado: **2** km/h.
- Opciones: 0, 2, 5, 10.

#### Debounce

Tiempo sobre el limite antes de emitir una sancion.

- Valor predeterminado: **250** ms.
- Opciones: 100, 250, 500, 1000.

#### Sancion por boxes

Sancion oficial enviada por exceso de velocidad en boxes.

- Valor predeterminado: **DRIVE_THROUGH**.
- Opciones: Drive-through, Stop and go, Descalificacion.

### Enforcement Avenex


#### Servicio DT/S&G Avenex

Controla drive-through y stop-and-go desde Avenex en lugar del HUD nativo AC/CSP.

- Valor predeterminado: **true**.
- Opciones: Activado, Desactivado.

#### Limite DT

Limite basado en la vuelta actual antes de escalar un DT incumplido a descalificacion.

- Valor predeterminado: **1** vueltas.
- Opciones: 1, 2, 3.

#### Tolerancia DT

Km/h extra permitidos sobre el limite de boxes al cumplir un drive-through.

- Valor predeterminado: **2** km/h.
- Opciones: 0, 2, 5, 10.

#### Limite pit fallback

Limite de velocidad fallback si el cliente no puede leer el valor de sesion.

- Valor predeterminado: **80** km/h.
- Opciones: 30, 50, 60, 80.

#### Limite S&G

Limite basado en la vuelta actual antes de escalar un stop and go incumplido a descalificacion.

- Valor predeterminado: **1** vueltas.
- Opciones: 1, 2, 3.

#### Detencion S&G

Segundos que el piloto debe quedar detenido en boxes.

- Valor predeterminado: **5** s.
- Opciones: 3, 5, 10, 15, 30.

#### Velocidad detenido

Velocidad maxima considerada detenido para contar el stop and go.

- Valor predeterminado: **1** km/h.
- Opciones: 0, 1, 2, 5.

### Tiempo post-carrera


#### Penalizaciones post-carrera

Suma los segundos sancionados a los resultados finales nativos y al reporte de auditoria.

- Valor predeterminado: **false**.
- Opciones: Activado, Desactivado.

#### Segundos por sancion

Segundos asignados al alcanzar el umbral de penalizacion de tiempo.

- Valor predeterminado: **1** s.
- Opciones: 0, 1, 2, 3, 5, 10.

### Enforcement nativo

El flujo actual solo usa enforcement nativo para descalificación. Los selectores heredados de DT y bloqueo no configuran el servicio propio de Avenex.

#### Enforcement nativo

Habilita el comando de descalificación nativa. No activa DT ni Stop & Go nativos.

- Valor predeterminado: **false**.
- Opciones: Activado, Desactivado.

#### Limite DT

Control heredado, sin efecto en el servicio DT/Stop & Go propio. Usa Avenex enforcement.

- Valor predeterminado: **2** vueltas.
- Opciones: 1, 2, 3.

#### Duracion de bloqueo

Control heredado, sin efecto en el servicio DT/Stop & Go propio. Usa Avenex enforcement.

- Valor predeterminado: **5** s.
- Opciones: 5, 10, 15, 30.

#### Mensajes de chat del servidor

Envia mensajes de sancion Avenex ademas del HUD nativo.

- Valor predeterminado: **true**.
- Opciones: Activado, Desactivado.

### Overlays del servidor


#### Overlays Avenex

Fuerza el encendido o apagado de los canales de overlay Avenex en los clientes conectados. Este valor del servidor pisa el INI local del cliente.

- Valor predeterminado: **true**.
- Opciones: Activado, Desactivado.

### Feedback HUD

Esta tarjeta no está disponible para configurar reglas en esta edición.

#### Monitor de incidentes

Muestra el monitor compacto de incidentes.

- Valor predeterminado: **true**.
- Opciones: Activado, Desactivado.

#### Monitor de cortes

Muestra el monitor compacto de cortes.

- Valor predeterminado: **true**.
- Opciones: Activado, Desactivado.

#### Banners de Race Control

Muestra overlays del canal Race Control Banner de Avenex.

- Valor predeterminado: **true**.
- Opciones: Activado, Desactivado.

#### Advisories de cumplimiento

Muestra overlays del canal Compliance Advisory de Avenex.

- Valor predeterminado: **true**.
- Opciones: Activado, Desactivado.

#### Monitor post-carrera

Muestra el monitor compacto de segundos post-carrera.

- Valor predeterminado: **false**.
- Opciones: Activado, Desactivado.

