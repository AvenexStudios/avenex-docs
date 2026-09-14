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
