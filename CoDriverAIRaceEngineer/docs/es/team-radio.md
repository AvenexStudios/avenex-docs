# Team Radio

Team Radio permite usar voz privada push-to-talk entre varios pilotos en
distintas PCs.

## Flujo básico

1. Un piloto crea un equipo.
2. Los demás pilotos se unen con el código de invitación.
3. Cada piloto selecciona micrófono y salida de audio.
4. Cada piloto asigna un input de push-to-talk.
5. Mantén presionado el input asignado para transmitir.

## Comportamiento esperado

- La app muestra el estado de conexión del equipo y presencia de miembros.
- Push-to-talk puede asignarse al teclado o a controles compatibles.
- Los dispositivos de audio pueden cambiarse con la app en ejecución.
- Si signaling o transporte de voz no están disponibles, la app debería mostrar
  estado degradado en lugar de cerrarse.

Team Radio usa el backend de signaling configurado por Avenex para descubrir el
equipo y WebRTC para transporte de voz.

## Prueba con dos PCs

Usa la misma build preliminar aprobada en ambas PCs.

1. Abre la app en ambas PCs.
2. En la PC 1, crea un equipo y copia el código de invitación.
3. En la PC 2, únete con ese código.
4. Confirma que ambos pilotos aparezcan en el roster.
5. Asigna push-to-talk en ambas PCs.
6. Mantén push-to-talk en la PC 1 y habla.
7. Repite desde la PC 2.
8. Cambia un dispositivo de audio mientras estás conectado y confirma que la voz
   siga funcionando.
9. Desconecta y reconecta una PC para confirmar que roster y voz se recuperen.

Si la voz no llega, confirma permisos del micrófono, dispositivos
seleccionados, permisos de red y que otra app no esté usando el micrófono de
manera exclusiva.
