# Server administration

Configure rules at `/avenex/admin` on your server's HTTP address. Keep access
credentials private.

## Saving and enabling rules
Save applies and stores your selections. Reload to confirm the saved values.
Import/export transfers settings, not served penalties or race results.
Back up settings before importing.

A field's server control has different effects:
- For an on/off setting, disabling its server control forces it off.
- For a penalty-ladder threshold, disabling its control disables that sanction.
- For other numeric selectors, disabling the control allows the client's local
  value. This does not mean zero. Keep scoring controls enabled for consistent
  league rules.

A field's Reset restores its default. The separate race-state reset clears
session points and sanction memory; it is not a configuration reset.
Changes do not recalculate past scores or penalties. The reaction and hold
values for a cut apply when that cut starts.

## Choosing a setup
Configure contact points first (defaults 1/2/3), then enable the ladder levels
and thresholds you want. Set pit service in Avenex enforcement, not in legacy
native controls. Enable post-race processing to apply accumulated penalty
seconds to final results.

For cuts, choose a count limit, service sanction, reaction margin, maximum
throttle, control duration and time per violation. Example: 1 s margin, 20%
throttle, 3 s control, +5 s. Excess throttle during the margin is allowed;
the first excess during control adds +5 s immediately.

For VSC/FCY, configure a speed limit and slowdown countdown separately from
the throttle rule for cuts. Do not rely on disabled cards.

See [penalty behavior](rules-and-sanctions.md), [incident scoring](incidents.md)
and [versions](versions.md).

## Settings
Defaults below are factory values, not necessarily your saved values.

### Penalty ladder


#### Contact points

Points per normal contact. Minimal contacts remain zero; changes apply only to new incidents.

- Default: **1** points.
- Choices: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

#### Heavy contact points

Points per heavy contact; does not change severity detection.

- Default: **2** points.
- Choices: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

#### Spin contact points

Points per contact with detected spin; a spin without contact is not an incident.

- Default: **3** points.
- Choices: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

#### Incident ladder

Apply official penalties from accumulated incident points.

- Default: **false**.
- Choices: Enabled, Disabled.

#### Warning at

Incident points needed before issuing a warning.

- Default: **8** points.
- Choices: 2, 4, 6, 8, 10, 12, 16.

#### Time penalty at

Incident points needed before adding post-race time.

- Default: **12** points.
- Choices: 2, 4, 6, 8, 10, 12, 16, 24.

#### Drive-through at

Incident points needed before issuing a drive-through.

- Default: **16** points.
- Choices: 2, 4, 6, 8, 10, 12, 16, 20, 24.

#### Stop and go at

Incident points needed before issuing a stop-and-go.

- Default: **20** points.
- Choices: 2, 4, 6, 8, 10, 12, 16, 20, 24, 30.

#### Disqualify at

Incident points needed before disqualification.

- Default: **30** points.
- Choices: 2, 4, 6, 8, 10, 16, 20, 24, 30, 40, 60.

### Track cuts


#### Track-cut rule

Count track-limit cuts independently from incident points.

- Default: **false**.
- Choices: Enabled, Disabled.

#### Cut limit

Count four-wheel excursions up to this limit, then pause cuts and throttle penalties until the sanction is served.

- Default: **3** cuts.
- Choices: 1, 2, 3, 4, 5, 6, 8, 10.

#### Reaction margin

Time after leaving the track to release the throttle. Throttle monitoring starts after this margin; the cut still counts.

- Default: **1000** ms.
- Choices: 0, 500, 1000, 1500, 2000, 3000, 5000.

#### Maximum throttle

Maximum throttle allowed during the hold period, after the reaction margin.

- Default: **10** %.
- Choices: 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100.

#### Throttle hold duration

Keep throttle at or below the maximum for this entire period after the reaction margin, even after rejoining.

- Default: **3** s.
- Choices: 1, 2, 3, 4, 5, 10, 15.

#### Throttle violation penalty

After the reaction margin, immediately add these seconds on the first throttle excess, once per cut. Monitoring stops at the cut limit.

- Default: **5** s.
- Choices: 1, 2, 3, 5, 10, 15, 20, 30, 60.

#### Cut sanction

Official penalty sent when the cut limit is reached.

- Default: **DRIVE_THROUGH**.
- Choices: Drive-through, Stop and go, Disqualification.

### Blue flags

This card is unavailable for configuring rules in this edition.

#### Blue-flag rule

Require yielding to the specific faster car behind.

- Default: **false**.
- Choices: Enabled, Disabled.

#### Yield window

Seconds before penalizing a missed blue flag.

- Default: **10** s.
- Choices: 5, 10, 15, 20.

#### Behind distance

Normalized track distance used to select the target behind.

- Default: **0.18** track.
- Choices: 0.08, 0.12, 0.18, 0.25.

#### Blue-flag sanction

Official penalty sent if the target is not yielded.

- Default: **DRIVE_THROUGH**.
- Choices: Drive-through, Stop and go, Disqualification.

### Yellow flags

This card is unavailable for configuring rules in this edition.

#### Yellow-flag rule

Require a speed drop while a caution flag is active.

- Default: **false**.
- Choices: Enabled, Disabled.

#### Slow-down window

Time available to reduce speed under yellow.

- Default: **3000** ms.
- Choices: 1000, 2000, 3000, 5000.

#### Required slow-down

Speed drop needed under yellow.

- Default: **10** km/h.
- Choices: 5, 10, 15, 20.

#### Yellow sanction

Official penalty sent if the driver does not slow.

- Default: **DRIVE_THROUGH**.
- Choices: Drive-through, Stop and go, Disqualification.

### Virtual safety car


#### VSC / FCY rule

Enable Avenex virtual safety car and full-course-yellow speed enforcement.

- Default: **false**.
- Choices: Enabled, Disabled.

#### Manual VSC active

Deploy or clear VSC from the server admin panel.

- Default: **false**.
- Choices: Enabled, Disabled.

#### VSC speed limit

Maximum speed while VSC is active.

- Default: **80** km/h.
- Choices: 40, 50, 60, 80, 100.

#### Slow-down countdown

Seconds available to slow down after VSC deploys.

- Default: **10** s.
- Choices: 5, 8, 10, 15, 20.

#### Speed tolerance

Extra km/h allowed over the VSC limit.

- Default: **3** km/h.
- Choices: 0, 2, 3, 5, 10.

#### Speeding debounce

Time above the VSC limit before issuing a penalty.

- Default: **500** ms.
- Choices: 250, 500, 1000, 2000.

#### VSC speeding sanction

Penalty sent if a driver exceeds the VSC limit after the countdown.

- Default: **DRIVE_THROUGH**.
- Choices: Drive-through, Stop and go, Disqualification.

#### Auto-deploy

Deploy VSC automatically from heavy incidents, multi-car clusters, or stopped cars.

- Default: **false**.
- Choices: Enabled, Disabled.

#### Cluster contacts

Nearby contact count needed to auto-deploy VSC.

- Default: **2** contacts.
- Choices: 2, 3, 4.

#### Cluster window

Time window used to group multi-car incidents.

- Default: **3000** ms.
- Choices: 1500, 2500, 3000, 5000.

#### Cluster distance

Maximum distance between contacts in the same VSC cluster.

- Default: **50** m.
- Choices: 25, 50, 75, 100.

#### Heavy-contact deploy

Impact speed that deploys VSC immediately.

- Default: **35** km/h.
- Choices: 25, 35, 45, 60.

#### Stopped speed

Speed treated as stopped for a post-contact car on track.

- Default: **5** km/h.
- Choices: 2, 5, 8, 10.

#### Stopped duration

How long a recently contacted car must remain stopped on track before VSC deploys.

- Default: **5000** ms.
- Choices: 3000, 5000, 8000, 10000.

#### Stopped contact window

Maximum age of the previous contact used to consider a stopped car hazardous.

- Default: **15000** ms.
- Choices: 10000, 15000, 20000, 30000.

#### Auto-clear delay

Seconds without a new hazard before auto VSC clears.

- Default: **20** s.
- Choices: 10, 20, 30, 45, 60.

### Pit speeding

This card is unavailable for configuring rules in this edition.

#### Pit-speeding rule

Detect pit-lane speeding from client telemetry.

- Default: **false**.
- Choices: Enabled, Disabled.

#### Tolerance

Speed allowed over the pit limit before enforcement.

- Default: **2** km/h.
- Choices: 0, 2, 5, 10.

#### Debounce

Time over the limit before a penalty is issued.

- Default: **250** ms.
- Choices: 100, 250, 500, 1000.

#### Pit-speeding sanction

Official penalty sent for pit-lane speeding.

- Default: **DRIVE_THROUGH**.
- Choices: Drive-through, Stop and go, Disqualification.

### Avenex enforcement


#### Avenex DT/S&G service

Track drive-through and stop-and-go service in Avenex instead of native AC/CSP HUD.

- Default: **true**.
- Choices: Enabled, Disabled.

#### DT deadline

Current-lap based deadline before missed DT escalates to disqualification.

- Default: **1** laps.
- Choices: 1, 2, 3.

#### DT speed tolerance

Extra km/h allowed over the pit limit while serving a drive-through.

- Default: **2** km/h.
- Choices: 0, 2, 5, 10.

#### Pit limit fallback

Fallback pit speed limit if the client cannot read the session value.

- Default: **80** km/h.
- Choices: 30, 50, 60, 80.

#### S&G deadline

Current-lap based deadline before missed stop-and-go escalates to disqualification.

- Default: **1** laps.
- Choices: 1, 2, 3.

#### S&G hold

Seconds the driver must stay stopped in pit lane.

- Default: **5** s.
- Choices: 3, 5, 10, 15, 30.

#### Stopped speed

Maximum speed treated as stopped for stop-and-go hold tracking.

- Default: **1** km/h.
- Choices: 0, 1, 2, 5.

### Post-race time


#### Post-race penalties

Add issued penalty seconds to native final race results and the audit report.

- Default: **false**.
- Choices: Enabled, Disabled.

#### Seconds per penalty

Seconds issued when the time penalty threshold is reached.

- Default: **1** s.
- Choices: 0, 1, 2, 3, 5, 10.

### Native enforcement

The current flow uses native enforcement only for disqualification. Legacy DT and hold selectors do not configure Avenex pit service.

#### Native enforcement

Enables the native disqualification command. Does not enable native DT or Stop & Go.

- Default: **false**.
- Choices: Enabled, Disabled.

#### DT deadline

Legacy setting, with no effect on Avenex DT/Stop & Go service. Use Avenex enforcement.

- Default: **2** laps.
- Choices: 1, 2, 3.

#### Hold duration

Legacy setting, with no effect on Avenex DT/Stop & Go service. Use Avenex enforcement.

- Default: **5** s.
- Choices: 5, 10, 15, 30.

#### Server chat messages

Send Avenex penalty chat messages in addition to native HUD.

- Default: **true**.
- Choices: Enabled, Disabled.

### Server overlays


#### Avenex overlays

Force Avenex overlay channels on or off for connected clients. This server value overrides the client local INI.

- Default: **true**.
- Choices: Enabled, Disabled.

### HUD feedback

This card is unavailable for configuring rules in this edition.

#### Incident monitor

Show the compact incident monitor.

- Default: **true**.
- Choices: Enabled, Disabled.

#### Cut monitor

Show the compact cuts monitor.

- Default: **true**.
- Choices: Enabled, Disabled.

#### Race Control Banners

Show Avenex Race Control Banner overlays.

- Default: **true**.
- Choices: Enabled, Disabled.

#### Compliance Advisories

Show Avenex Compliance Advisory overlays.

- Default: **true**.
- Choices: Enabled, Disabled.

#### Post-race monitor

Show the compact post-race seconds monitor.

- Default: **false**.
- Choices: Enabled, Disabled.

