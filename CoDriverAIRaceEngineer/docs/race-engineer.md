# Race Engineer

The race engineer answers approved English questions using local speech
recognition, live telemetry, and local voice playback.

## Supported style

Ask short race-context questions such as:

| Topic | Example questions |
| ----- | ----------------- |
| Position | What is my position? Where am I? |
| Gaps | What is the gap ahead? What is the gap behind? |
| Session | How many laps left? How long left? |
| Pace | What was my last lap? What is my best lap? What lap am I on? |
| Fuel | How much fuel? How many laps of fuel do I have left? |
| Car state | What gear am I in? What is my speed? What are my RPM? |
| Conditions | What is the track temperature? What is the air temperature? |
| Controls | Say again. Repeat that. Keep quiet. Keep me informed. |

The preview is deterministic: answers come from known question patterns and
available telemetry rather than free-form live analysis.

Some questions depend on telemetry fields that may not be available in every
session. When data is missing, the engineer should say that it does not have the
data instead of guessing.

## Voice

Voice recognition and voice playback run locally. The app may need to prepare
local resources before the engineer is ready.

If telemetry is unavailable, the engineer may answer with a short missing-data
message instead of guessing.
