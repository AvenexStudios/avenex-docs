# Reglas y sanciones

Actualizado: 2026-09-10. La configuracion efectiva del servidor manda sobre los
valores locales cuando su control de servidor esta activo.

## Advertencia

Avisa de que se alcanzo el umbral de puntos configurado. No obliga a entrar en
boxes ni agrega segundos. La escala emite cada nivel una vez por estado de
carrera; reiniciar el estado permite volver a emitirlo.

## Penalizacion de tiempo

Suma segundos al resultado, no exige detenerse ni reduce la velocidad del auto.
El banner anuncia los segundos emitidos; el Status Monitor muestra el total
acumulado, no los puntos de incidente. Se oculta cuando no hay tiempo pendiente.

La escala de incidentes emite el importe configurado al alcanzar su umbral.
No se multiplica por los puntos: un umbral de 2 puntos y una sancion de 3 s
significan +3 s, no +6 s. Un cambio posterior del selector no altera lo emitido.

Cada incumplimiento de acelerador por cortes puede sumar otro importe.
Ejemplo: +3 s de escala y dos incumplimientos de +5 s producen +13 s.
Servir DT o S&G no borra esos segundos.

Con el procesamiento post-carrera activo, Avenex aplica los segundos emitidos
a los tiempos finales y recalcula el orden respetando las vueltas completadas.
El HTML conserva tiempo original, recargo y tiempo ajustado. No use el tiempo
de una vuelta aislada para compararlo con el tiempo total de carrera.

El reporte es `cfg/avenex_post_race_results.html`, dentro de la instalacion del
servidor. Se reemplaza con el ultimo reporte generado: archive una copia para
conservar evidencia. Se genera al finalizar los resultados, cuando terminaron
los participantes activos pertinentes o vencio la espera de fin de carrera;
no requiere comenzar otra carrera. La IA dinamica puede cambiar la lista de
participantes. El modo sin loop debe verificarse con el cierre efectivo de la
sesion, no solo con el cruce del primer auto.

## Drive-through

El piloto debe cumplir la obligacion en boxes dentro del plazo de vueltas
configurado. Avenex muestra una obligacion pendiente y luego el banner Served.
Si vence sin servir, escala a DSQ y puede expulsar al piloto.

Limitacion vigente: el reconocimiento actual comprueba presencia en pit lane
y velocidad dentro del limite mas tolerancia; no certifica un recorrido completo
desde la entrada hasta la salida. No confundir la prueba aprobada del flujo
con una validacion exhaustiva de ese recorrido.

## Stop & Go

El piloto debe quedar detenido en boxes durante los segundos configurados en
Avenex enforcement / S&G hold. El limite de velocidad considerado detenido es
configurable. Si acelera y deja de cumplir la condicion antes de terminar,
el contador de detencion vuelve al inicio. Al completar el tiempo se sirve.
Al vencer el plazo sin cumplir, escala a DSQ.

No teletransporta el auto a boxes ni bloquea el acelerador: el piloto debe
cumplirlo. El bloqueo nativo legado no configura este servicio propio.

## Descalificacion

Es la sancion terminal y la unica via de enforcement nativo usada por el flujo
actual. Dependiendo de la configuracion, se envia el comando nativo de DSQ o
se aplica la expulsion del servidor. No es una sancion que se pueda servir.

## Cortes de pista

Cada salida con las cuatro ruedas cuenta inmediatamente una vez. Permanecer
fuera no repite el corte; volver a pista y salir otra vez puede sumar otro.
Cumplir la regla del acelerador no perdona ni borra el corte.

1. Se suma el corte y empieza el margen de reaccion configurable.
2. Terminado el margen, comienza el periodo de control.
3. Durante ese periodo, el primer exceso del porcentaje de acelerador permitido
   suma inmediatamente el tiempo configurado, una vez por corte.
4. Respetar el maximo hasta terminar evita ese recargo, pero conserva el corte.

Volver a pista no cancela una obligacion de acelerador vigente. Los limites de
ruedas y acelerador dependen de la telemetria disponible, no de juzgar culpa.

Al alcanzar el limite de cortes, se emite DT, S&G o DSQ segun el selector.
Se congela el contador y se cancelan controles de acelerador pendientes:
no siguen sumandose cortes ni recargos mientras esa sancion esta pendiente.
Al servir el DT/S&G correspondiente, solo el contador de cortes vuelve a cero.
Los segundos anteriores permanecen; nuevos cortes posteriores pueden sumar mas.

## Escala de incidentes

Los puntos acumulados y los cortes son contadores separados.
Elija que niveles habilitar: advertencia, tiempo, DT, S&G y DSQ.
Si un incidente atraviesa varios umbrales, se elige el nivel mas alto alcanzado,
no todas las sanciones intermedias. Ajuste los umbrales a la puntuacion elegida.

El servicio mantiene una unica obligacion DT/S&G pendiente: no implementa una
cola de multiples obligaciones identicas. Las sanciones emitidas no cambian
retroactivamente al editar el admin.

## Otras reglas del admin

- **VSC/FCY:** permite neutralizar con velocidad maxima y un margen para reducirla.
  Puede activarse manualmente; la opcion automatica considera incidentes
  agrupados y autos detenidos tras contactos. No es un safety car fisico.
  Mantener estas opciones en pruebas hasta su aceptacion especifica.
- **Bandera azul:** plantea ceder a un auto mas rapido identificado detras,
  con plazo y sancion configurables. Tarjeta no implementada en el admin.
- **Bandera amarilla:** plantea reduccion de velocidad bajo precaucion,
  con margen y sancion. Tarjeta no implementada; no sustituye la regla de cortes.
- **Exceso en boxes:** considera limite, tolerancia y duracion del exceso antes
  de sancionar. Tarjeta no implementada en el admin.
- **Overlays:** ocultarlos no debe interpretarse como haber servido o eliminado
  una sancion. El master visual es distinto de las reglas de carrera.

## Evidencia y aprobaciones

El propietario aprobo la etapa funcional de cortes el 2026-09-10 (RULE-T03).
Tambien reporto pruebas satisfactorias de DT, S&G, DSQ y resultados de tiempo.
Esto no aprueba automaticamente deteccion de todos los accidentes, VSC,
banderas, ni el arte final de los overlays. Los nuevos selectores de puntuacion
requieren su prueba in-game. Las capturas de la galeria pendientes siguen
pendientes: no se sustituyen por imagenes inventadas.

Consulte la [referencia completa del admin](server-admin.md),
[incidentes y severidad](incidents.md) y la [galeria](overlays/gallery.md).

