# Troubleshooting

Operational checks for the current Avenex Race Control build.

## First Checks

- Confirm the Assetto Corsa Lua app is enabled.
- Confirm the server plugin is loaded.
- Confirm the client joined an Avenex-enabled online session.
- Confirm the server-admin panel applied the expected configuration.

## Puntos o tiempo inesperados

Compruebe los valores guardados y los controles de servidor, no solo lo mostrado
antes de pulsar Guardar. Un cambio afecta nuevos incidentes; no recalcula los
anteriores. El tiempo acumulado no se multiplica por puntos y no desaparece al
servir DT/S&G. Los recargos de cortes y de la escala se suman.

## Cortes

El corte se cuenta al salir con cuatro ruedas, no al acabar el contador.
El margen permite reaccionar; terminado el margen, un exceso de acelerador
durante el control penaliza inmediatamente. Al limite, el contador se congela.
Solo servir la sancion de ese limite permite volver a cero.

## Reporte

Abra el archivo cfg/avenex_post_race_results.html del servidor y revise su fecha
de modificacion. Recargue el navegador; no compare con una copia archivada de
otra carrera. El reporte depende de la finalizacion de resultados, no solo del
primer piloto que cruza la meta. Compare tiempos totales, vueltas y recargos.

## Admin disponible pero juego inaccesible

El panel HTTP y la conexion del juego usan servicios/puertos distintos.
Compruebe el proceso AssettoServer, puerto HTTP, puertos TCP/UDP configurados
y si el enlace apunta a la direccion local o publica correcta.
No suponga que un panel accesible prueba conectividad del juego.

## Cambios de cliente y rendimiento

Despues de desplegar archivos Lua vuelva a entrar para cargar la nueva version.
No active el recorder de forma permanente: se usa para una prueba diagnostica
acotada y puede agregar carga. Conserve los registros de sesion/error antes de
limpiar el estado; no publique tokens ni datos de acceso.
