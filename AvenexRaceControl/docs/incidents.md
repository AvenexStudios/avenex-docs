# Incidents and severity

Avenex counts involvement in accidents, not fault or intent.

## What counts
An incident requires evidence of contact involving the driver. A close pass,
another car braking, or a speed change alone should not count as a collision.
Several observations from the same accident are grouped to avoid charging
each one separately. Processing can take a short time after the impact.

Missing information can limit detection. Report an apparent missed contact or
false positive to your administrator with the session and a description.

## Severity
Severity considers impact intensity, relative speed, speed loss associated with
the collision and whether an involved car spins. Another car slowing down
does not replace the need for contact. A spin without contact does not create
a contact incident by itself.

| Category | Meaning | Default points |
| --- | --- | --- |
| Minimal | Very small contact | 0 |
| Light/normal | Contact above the minimal category | 1 |
| Heavy | Stronger impact or substantial associated speed loss | 2 |
| Contact with spin | Contact with an associated spin | 3 |

## Points and penalties
Administrators can choose 0..10 points for light/normal, heavy and spin contacts.
Changing points does not change how severity is determined. A zero-point
contact can still be recorded.

With server controls enabled, new incidents use the server's configured score.
Previously awarded points and penalties are not recalculated. Keep server
controls enabled for uniform league scoring.

Incident points feed the penalty ladder. Track cuts have a separate counter.
See [penalties](rules-and-sanctions.md) and [admin settings](server-admin.md).

