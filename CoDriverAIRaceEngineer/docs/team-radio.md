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
