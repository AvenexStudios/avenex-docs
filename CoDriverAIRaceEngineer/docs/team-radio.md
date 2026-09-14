# Team Radio

Team Radio lets drivers use private push-to-talk voice across multiple PCs.

## Basic flow

1. One driver creates a team.
2. Other drivers join with the invite code.
3. Each driver selects microphone and output devices.
4. Each driver binds a push-to-talk input.
5. Hold the bound input to transmit.

## Expected behavior

- The app shows team connection state and member presence.
- Push-to-talk can be bound to keyboard or supported controller inputs.
- Audio device changes can be made while the app is running.
- If signaling or voice transport is unavailable, the app should show degraded
  state instead of crashing.

Team Radio uses the configured Avenex signaling backend for team discovery and
WebRTC for voice transport.

## Two-PC test

Use the same approved preview build on both PCs.

1. Launch the app on both PCs.
2. On PC 1, create a team and copy the invite code.
3. On PC 2, join with that code.
4. Confirm both drivers appear in the roster.
5. Bind push-to-talk on both PCs.
6. Hold push-to-talk on PC 1 and speak.
7. Repeat from PC 2.
8. Change an audio device while connected and confirm voice still works.
9. Disconnect and reconnect one PC to confirm the roster and voice recover.

If voice does not arrive, confirm microphone permissions, selected devices,
network permissions, and that only one app is using the microphone exclusively.
