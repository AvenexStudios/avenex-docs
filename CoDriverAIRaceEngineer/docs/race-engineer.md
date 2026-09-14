# Race Engineer

The race engineer answers approved English questions using local speech
recognition, live telemetry, and local voice playback.

## Supported style

Ask short race-context questions such as:

- What is my position?
- What is my fuel?
- What is my lap time?
- What gear am I in?
- What is my speed?

The preview is deterministic: answers come from known question patterns and
available telemetry rather than free-form live analysis.

## Voice

Voice recognition and voice playback run locally. The app may need to prepare
local resources before the engineer is ready.

If telemetry is unavailable, the engineer may answer with a short missing-data
message instead of guessing.
